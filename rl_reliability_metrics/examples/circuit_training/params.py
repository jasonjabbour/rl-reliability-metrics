# coding=utf-8
# Copyright 2019 The Authors of RL Reliability Metrics.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Parameters for "TF-Agents Mujoco Subset" example."""

import os

# Information about the data we are evaluating.
data_source = 'csv'  # or 'tensorboard' to load the Tensorboard example data
algos = ['ppo_111', 'ppo_222', 'ppo_333']
tasks = ['circuittraining']
runs = ['0', '1', '2']
n_runs_per_experiment = 3

# Base directory for data and results.
home = os.path.expanduser('~')
base_dir = os.path.join(home, 'Jason/RLPerf/rl-reliability-metrics/rl_reliability_metrics/examples/circuit_training')

# Path to downloaded example TF-Agents MuJoCo data.
data_dir = os.path.join(base_dir, 'data')

# Paths to results and intermediate results.
results_dir = os.path.join(base_dir, 'results')
metric_values_dir = os.path.join(results_dir, 'metric_values')
metric_values_dir_permuted = os.path.join(results_dir, 'metric_values_permuted')
metric_values_dir_bootstrapped = os.path.join(results_dir,
                                              'metric_values_bootstrapped')
pvals_dir = os.path.join(results_dir, 'stats_comparisons')
confidence_intervals_dir = os.path.join(results_dir,
                                        'stats_confidence_intervals')
plots_dir = os.path.join(results_dir, 'plots')

# Path to gin config file.
gin_file = 'rl_reliability_metrics/evaluation/example.gin'

# Which metrics to evaluate.
metrics = [
    'IqrWithinRuns', 'LowerCVaROnDiffs', 'LowerCVaROnDrawdown', 'IqrAcrossRuns',
    'LowerCVaROnAcross', 'MedianPerfDuringTraining'
]
# These metrics only have one value per training run:
metrics_no_timeframes = ['LowerCVaROnDiffs', 'LowerCVaROnDrawdown']
# These metrics are evaluated at multiple timepoints per training run:
metrics_with_timeframes = [
    'IqrWithinRuns', 'IqrAcrossRuns', 'LowerCVaROnAcross',
    'MedianPerfDuringTraining'
]

# How to collapse across timepoints for displaying results.
# - Divide each training run into 3 "timeframes" -- beginning, middle, and end.
n_timeframes = 3
timeframes = range(n_timeframes)

# Parameters for permutations / bootstraps
n_random_samples = 5  # Normally this should be >= 1000
n_worker = 1
