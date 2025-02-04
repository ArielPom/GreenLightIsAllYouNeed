import matplotlib.pyplot as plt
import pandas as pd

class EpisodesData :
    def __init__(self):
        self.episodes = 0
        self.arrived_vehicles = []
        self.total_waiting_times = []
        self.avg_speeds = []

    def add_episode_data(self, simulation):
        self.episodes += 1
        self.arrived_vehicles.append(simulation.arrived_vehicles)
        self.total_waiting_times.append(simulation.total_waiting_time)
        self.avg_speeds.append(simulation.avg_speed)

    def plot_action_probabilities(self, probs_file, episode):
        df = pd.read_csv(probs_file)
        episode_df = df[df["episode"] == episode]
        plt.figure(figsize=(12, 5))
        plt.plot(episode_df["step"], episode_df["prob0"], marker="o", linestyle="-", label="Prob 0", color="blue")
        plt.title(f"Episode {episode} - Probability of Action 0 vs Step")
        plt.xlabel("Step")
        plt.ylabel("Probability 0")
        plt.grid(True)
        plt.ylim(0, 1)
        plt.show()

    def plot_training_results(self):

        # create a plot with 3 subplots :
        #                   waiting time per episode
        #                   average speed per episode
        #                   total vehicles arrived per episode

        fig, axs = plt.subplots(3, figsize=(10, 12))
        fig.suptitle('Training Results')
        axs[0].plot(self.total_waiting_times)
        axs[0].set_title('Total Waiting Time per Episode')
        axs[0].set(xlabel='Episode', ylabel='Total Waiting Time')

        axs[1].plot(self.arrived_vehicles)
        axs[1].set_title('Number of Vehicles Arrived per Episode')
        axs[1].set(xlabel='Episode', ylabel='Average Speed')

        axs[2].plot(self.avg_speeds)
        axs[2].set_title('Average Speed per Episode')
        axs[2].set(xlabel='Episode', ylabel='Total Vehicles Arrived')

        for ax in axs.flat:
            ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
            ax.grid(True)

        plt.subplots_adjust(hspace=1)
        plt.show()
    

if __name__ == '__main__':
    episodes_data = EpisodesData()
    episodes_data.plot_action_probabilities("probs_history.csv", 190)