# src/goals.py

from typing import List, Optional, Tuple


def max_window_sum(arr: List[int], k: int) -> Optional[Tuple[int, int]]:
    """
    Find the subarray of length k with the maximum sum.
    Returns a tuple (start_index, max_sum), or None if k > len(arr).
    Raises ValueError if k <= 0.
    """
    if k <= 0:
        raise ValueError("Window size k must be positive")

    n = len(arr)
    if k > n:
        return None

    # first window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    max_index = 0

    # slide window
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i - k + 1

    return max_index, max_sum


def count_goal_windows(arr: List[int], k: int, threshold: float) -> int:
    """
    Count the number of windows of size k whose average >= threshold.
    Returns 0 if k > len(arr).
    Raises ValueError if k <= 0.
    """
    if k <= 0:
        raise ValueError("Window size k must be positive")

    n = len(arr)
    if k > n:
        return 0

    target_sum = threshold * k
    count = 0

    current_sum = sum(arr[:k])
    if current_sum >= target_sum:
        count += 1

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum >= target_sum:
            count += 1

    return count


def longest_rising_streak(arr: List[int]) -> int:
    """
    Return the length of the longest strictly increasing consecutive subsequence.
    """
    if not arr:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak
