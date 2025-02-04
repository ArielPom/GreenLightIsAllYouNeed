import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

route_ids = ["E7_E6", "E9_E8", "E6_E7", "E8_E9"]
ROUTES_STRING = f"""<routes>
    <route id="{route_ids[0]}" edges="-E7 -E6"/>
    <route id="{route_ids[1]}" edges="-E9 -E8"/>
    <route id="{route_ids[2]}" edges="E6 E7"/>
    <route id="{route_ids[3]}" edges="E8 E9"/>
"""

class TrafficGenerator:
    def __init__(self, rou_file_path, max_sim_time, step_length, n_cars_generated, seed=None, distribution="normal"):
        self._rou_file_path = rou_file_path
        self._max_sim_time = max_sim_time
        self._step_length = step_length
        self._max_steps = int(max_sim_time / step_length)
        self._n_cars_generated = n_cars_generated
        self._seed = seed
        self._timings = None
        self._distribution = distribution

        # normal distribution
        self._mean_1 = self._max_sim_time * (3 / 10)
        self._mean_2 = self._max_sim_time * (7 / 10)
        self._std_dev_1 = self._max_sim_time / 8
        self._std_dev_2 = self._max_sim_time / 10
        self._n_cars_1 = int(self._n_cars_generated * (1/2))
        self._n_cars_2 = int(self._n_cars_generated * (1/2))

        if self._distribution == "normal":
            self.generate_normal_distribution_timings()
        elif self._distribution == "uniform":
            self.generate_random_timings()

    def generate_random_timings(self):
        if self._seed is not None:
            np.random.seed(self._seed)
        self._timings = np.random.uniform(0, self._max_sim_time, self._n_cars_generated)
        self._timings = np.sort(self._timings)

    def generate_normal_distribution_timings(self):
        if self._seed is not None:
            np.random.seed(self._seed)
        timings1 = np.random.normal(self._mean_1, self._std_dev_1, int(self._n_cars_1))
        timings2 = np.random.normal(self._mean_2, self._std_dev_2, int(self._n_cars_2))
        timings = np.concatenate((timings1, timings2))
        timings = np.clip(timings, 0, self._max_sim_time)
        self._timings = np.sort(timings)

    def generate_routefile(self, plot_distribution=False):
        car_gen_steps = np.round(self._timings, 1)
        with open(self._rou_file_path, "w") as routes:
            print(ROUTES_STRING, file=routes)
            for car_counter, step in enumerate(car_gen_steps):
                route = np.random.choice(route_ids)
                print(f'    <vehicle id="{car_counter}" route="{route}" '
                      f'depart="{step}" departLane="random" departSpeed="max" />', file=routes)
            print("</routes>", file=routes)
        if plot_distribution:
            self.plot_distribution()

    def plot_distribution(self):
        plt.figure(figsize=(10, 5))
        bins_num = int(self._max_sim_time / 10)

        # Create primary axis (number of cars)
        ax1 = plt.gca()
        
        # Histogram of generated timings (number of cars)
        ax1.hist(self._timings, bins=bins_num, density=False, alpha=0.6, color='b', label="Number of Cars")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Number of Cars", color='b')
        ax1.tick_params(axis='y', labelcolor='b')

        # Create secondary axis (PDF)
        ax2 = ax1.twinx()  # Create a twin axis sharing the x-axis
        x = np.linspace(0, self._max_sim_time, 1000)

        # Compute the chosen probability density function
        if self._distribution == "normal":
            pdf1 = norm.pdf(x, self._mean_1, self._std_dev_1)
            pdf2 = norm.pdf(x, self._mean_2, self._std_dev_2)
            pdf = (1/2) * pdf1 + (1/2) * pdf2  # Weighted sum
        elif self._distribution == "uniform":
            pdf = np.ones_like(x) / self._max_sim_time

        # Plot the probability density function
        ax2.plot(x, pdf, 'r-', label="Probability Density Function")
        ax2.set_ylabel("Density", color='r')
        ax2.tick_params(axis='y', labelcolor='r')

        # Legends and formatting
        ax1.legend(loc="upper left")
        ax2.legend(loc="upper right")
        plt.title("Distribution of Vehicle Departures")
        plt.grid(True)
        plt.show()