import numpy as np
import torch
from collections import deque


class ReplayBuffer:
    def __init__(self, capacity):
        self._capacity = capacity
        self._buffer = deque(maxlen=self._capacity)
        self._size = 0

    def add_sample(self, sample):
        if self._size < self._capacity:
            self._buffer.append(sample)
            self._size += 1
        else:
            self._buffer.popleft()
            self._buffer.append(sample)
        
    def sample(self, batch_size):
        if self._size < batch_size:
            return None
        else:
            indices = np.random.choice(self._size, batch_size, replace=False)
            batch =  [self._buffer[idx] for idx in indices]
            states, actions, prev_log_probs, log_probs, rewards, next_states = zip(*batch)

            print(f"states type: {type(states)}")
            print(f"actions type: {type(actions)}")
            print(f"prev_log_probs type: {type(prev_log_probs)}")
            print(f"log_probs type: {type(log_probs)}")
            print(f"rewards type: {type(rewards)}")
            print(f"next_states type: {type(next_states)}")
            

            states = torch.tensor(np.array(states), dtype=torch.float32)
            actions = torch.tensor(np.array(actions), dtype=torch.int32)
            rewards = torch.tensor(np.array(rewards), dtype=torch.float32)
            next_states = torch.tensor(np.array(next_states), dtype=torch.float32)

            prev_log_probs = torch.stack([x.detach() for x in prev_log_probs])
            log_probs = torch.stack([x.detach() for x in log_probs])

            return states, actions, prev_log_probs, log_probs, rewards, next_states
