import json
import matplotlib.pyplot as plt

# The JSON data provided
json_data = '''
{
  "best_metric": null,
  "best_model_checkpoint": null,
  "epoch": 2.0,
  "global_step": 1400,
  "is_hyper_param_search": false,
  "is_local_process_zero": true,
  "is_world_process_zero": true,
  "log_history": [
    {
      "epoch": 0.0,
      "learning_rate": 4.996428571428572e-05,
      "loss": 19.3111,
      "step": 1
    },
    {
      "epoch": 0.0,
      "learning_rate": 4.996428571428572e-05,
      "loss": 19.3637,
      "step": 2
    },
    {
      "epoch": 0.0,
      "learning_rate": 4.996428571428572e-05,
      "loss": 19.4483,
      "step": 3
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.996428571428572e-05,
      "loss": 18.2149,
      "step": 4
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.996428571428572e-05,
      "loss": 21.7095,
      "step": 5
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.992857142857143e-05,
      "loss": 20.1326,
      "step": 6
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.989285714285715e-05,
      "loss": 13.4286,
      "step": 7
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.985714285714286e-05,
      "loss": 11.8196,
      "step": 8
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.982142857142857e-05,
      "loss": 11.4361,
      "step": 9
    },
    {
      "epoch": 0.01,
      "learning_rate": 4.978571428571429e-05,
      "loss": 10.1669,
      "step": 10
    },
    {
      "epoch": 0.01,
      "eval_cer": 0.979559331032652,
      "eval_loss": 9.360828399658203,
      "eval_runtime": 324.0175,
      "eval_samples_per_second": 0.719,
      "eval_steps_per_second": 0.361,
      "step": 10
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.975e-05,
      "loss": 9.8843,
      "step": 11
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.971428571428572e-05,
      "loss": 8.7883,
      "step": 12
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.967857142857143e-05,
      "loss": 8.3293,
      "step": 13
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.964285714285715e-05,
      "loss": 8.0922,
      "step": 14
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.960714285714286e-05,
      "loss": 8.2891,
      "step": 15
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.957142857142857e-05,
      "loss": 7.0987,
      "step": 16
    },
    {
      "epoch": 0.02,
      "learning_rate": 4.953571428571429e-05,
      "loss": 8.319,
      "step": 17
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.9500000000000004e-05,
      "loss": 7.2722,
      "step": 18
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.946428571428572e-05,
      "loss": 7.2545,
      "step": 19
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.942857142857143e-05,
      "loss": 6.3778,
      "step": 20
    },
    {
      "epoch": 0.03,
      "eval_cer": 0.984669498274489,
      "eval_loss": 6.0216755867004395,
      "eval_runtime": 317.1006,
      "eval_samples_per_second": 0.735,
      "eval_steps_per_second": 0.369,
      "step": 20
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.939285714285714e-05,
      "loss": 5.8069,
      "step": 21
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.935714285714286e-05,
      "loss": 6.6587,
      "step": 22
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.9321428571428574e-05,
      "loss": 6.0239,
      "step": 23
    },
    {
      "epoch": 0.03,
      "learning_rate": 4.928571428571429e-05,
      "loss": 5.6921,
      "step": 24
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.9250000000000004e-05,
      "loss": 5.4328,
      "step": 25
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.921428571428572e-05,
      "loss": 5.6522,
      "step": 26
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.917857142857143e-05,
      "loss": 5.8568,
      "step": 27
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.9142857142857144e-05,
      "loss": 5.4906,
      "step": 28
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.910714285714286e-05,
      "loss": 5.3816,
      "step": 29
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.9071428571428574e-05,
      "loss": 4.9719,
      "step": 30
    },
    {
      "epoch": 0.04,
      "eval_cer": 0.9694053623573136,
      "eval_loss": 4.858269691467285,
      "eval_runtime": 339.1832,
      "eval_samples_per_second": 0.687,
      "eval_steps_per_second": 0.345,
      "step": 30
    },
    {
      "epoch": 0.04,
      "learning_rate": 4.903571428571429e-05,
      "loss": 4.7084,
      "step": 31
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.9e-05,
      "loss": 4.3499,
      "step": 32
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.896428571428572e-05,
      "loss": 5.0402,
      "step": 33
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.892857142857143e-05,
      "loss": 4.6763,
      "step": 34
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.8892857142857144e-05,
      "loss": 4.6732,
      "step": 35
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.885714285714286e-05,
      "loss": 4.4368,
      "step": 36
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.8821428571428575e-05,
      "loss": 4.5732,
      "step": 37
    },
    {
      "epoch": 0.05,
      "learning_rate": 4.878571428571429e-05,
      "loss": 4.59,
      "step": 38
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.875e-05,
      "loss": 4.6247,
      "step": 39
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.8714285714285714e-05,
      "loss": 4.6976,
      "step": 40
    },
    {
      "epoch": 0.06,
      "eval_cer": 0.9758428457658614,
      "eval_loss": 4.459213733673096,
      "eval_runtime": 326.93,
      "eval_samples_per_second": 0.713,
      "eval_steps_per_second": 0.358,
      "step": 40
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.867857142857143e-05,
      "loss": 4.5293,
      "step": 41
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.8642857142857145e-05,
      "loss": 4.3626,
      "step": 42
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.860714285714286e-05,
      "loss": 4.283,
      "step": 43
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.8571428571428576e-05,
      "loss": 4.3732,
      "step": 44
    },
    {
      "epoch": 0.06,
      "learning_rate": 4.853571428571429e-05,
      "loss": 4.3608,
      "step": 45
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.85e-05,
      "loss": 4.1953,
      "step": 46
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.8464285714285715e-05,
      "loss": 4.623,
      "step": 47
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.842857142857143e-05,
      "loss": 4.7934,
      "step": 48
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.8392857142857146e-05,
      "loss": 4.749,
      "step": 49
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.835714285714286e-05,
      "loss": 4.3268,
      "step": 50
    },
    {
      "epoch": 0.07,
      "eval_cer": 0.955468542606849,
      "eval_loss": 4.198706150054932,
      "eval_runtime": 329.5189,
      "eval_samples_per_second": 0.707,
      "eval_steps_per_second": 0.355,
      "step": 50
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.832142857142857e-05,
      "loss": 4.2632,
      "step": 51
    },
    {
      "epoch": 0.07,
      "learning_rate": 4.828571428571429e-05,
      "loss": 4.9617,
      "step": 52
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.825e-05,
      "loss": 4.2956,
      "step": 53
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.8214285714285716e-05,
      "loss": 4.4607,
      "step": 54
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.817857142857143e-05,
      "loss": 4.0713,
      "step": 55
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.8142857142857147e-05,
      "loss": 4.1747,
      "step": 56
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.810714285714286e-05,
      "loss": 4.216,
      "step": 57
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.807142857142857e-05,
      "loss": 4.3623,
      "step": 58
    },
    {
      "epoch": 0.08,
      "learning_rate": 4.803571428571429e-05,
      "loss": 4.293,
      "step": 59
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.8e-05,
      "loss": 4.3978,
      "step": 60
    },
    {
      "epoch": 0.09,
      "eval_cer": 0.968608972657287,
      "eval_loss": 4.037250518798828,
      "eval_runtime": 318.8079,
      "eval_samples_per_second": 0.731,
      "eval_steps_per_second": 0.367,
      "step": 60
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.7964285714285717e-05,
      "loss": 3.9851,
      "step": 61
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.7928571428571425e-05,
      "loss": 4.1221,
      "step": 62
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.789285714285715e-05,
      "loss": 4.0313,
      "step": 63
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.785714285714286e-05,
      "loss": 4.3526,
      "step": 64
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.782142857142857e-05,
      "loss": 4.0907,
      "step": 65
    },
    {
      "epoch": 0.09,
      "learning_rate": 4.7785714285714287e-05,
      "loss": 3.981,
      "step": 66
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.775e-05,
      "loss": 3.9979,
      "step": 67
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.771428571428572e-05,
      "loss": 4.1374,
      "step": 68
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.767857142857143e-05,
      "loss": 3.9689,
      "step": 69
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.764285714285715e-05,
      "loss": 4.1322,
      "step": 70
    },
    {
      "epoch": 0.1,
      "eval_cer": 0.955468542606849,
      "eval_loss": 3.7960362434387207,
      "eval_runtime": 336.4386,
      "eval_samples_per_second": 0.693,
      "eval_steps_per_second": 0.348,
      "step": 70
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.760714285714286e-05,
      "loss": 3.8558,
      "step": 71
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.757142857142857e-05,
      "loss": 3.7872,
      "step": 72
    },
    {
      "epoch": 0.1,
      "learning_rate": 4.753571428571429e-05,
      "loss": 4.0053,
      "step": 73
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.75e-05,
      "loss": 3.7827,
      "step": 74
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.746428571428572e-05,
      "loss": 3.8724,
      "step": 75
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.742857142857143e-05,
      "loss": 3.64,
      "step": 76
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.739285714285714e-05,
      "loss": 3.6433,
      "step": 77
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.7357142857142864e-05,
      "loss": 3.778,
      "step": 78
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.732142857142857e-05,
      "loss": 3.629,
      "step": 79
    },
    {
      "epoch": 0.11,
      "learning_rate": 4.728571428571429e-05,
      "loss": 4.2069,
      "step": 80
    },
    {
      "epoch": 0.11,
      "eval_cer": 0.9899787629413326,
      "eval_loss": 3.6565685272216797,
      "eval_runtime": 319.9921,
      "eval_samples_per_second": 0.728,
      "eval_steps_per_second": 0.366,
      "step": 80
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.7249999999999997e-05,
      "loss": 3.6515,
      "step": 81
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.721428571428572e-05,
      "loss": 3.5265,
      "step": 82
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.7178571428571434e-05,
      "loss": 3.5304,
      "step": 83
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.714285714285714e-05,
      "loss": 3.5407,
      "step": 84
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.710714285714286e-05,
      "loss": 3.8785,
      "step": 85
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.707142857142857e-05,
      "loss": 3.6663,
      "step": 86
    },
    {
      "epoch": 0.12,
      "learning_rate": 4.703571428571429e-05,
      "loss": 4.1695,
      "step": 87
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.7e-05,
      "loss": 3.6414,
      "step": 88
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.696428571428572e-05,
      "loss": 4.1027,
      "step": 89
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.6928571428571435e-05,
      "loss": 3.5302,
      "step": 90
    },
    {
      "epoch": 0.13,
      "eval_cer": 0.968741704273958,
      "eval_loss": 3.3807404041290283,
      "eval_runtime": 313.848,
      "eval_samples_per_second": 0.742,
      "eval_steps_per_second": 0.373,
      "step": 90
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.689285714285714e-05,
      "loss": 3.4434,
      "step": 91
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.685714285714286e-05,
      "loss": 3.5472,
      "step": 92
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.6821428571428574e-05,
      "loss": 3.3496,
      "step": 93
    },
    {
      "epoch": 0.13,
      "learning_rate": 4.678571428571429e-05,
      "loss": 3.3518,
      "step": 94
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.6750000000000005e-05,
      "loss": 3.5571,
      "step": 95
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.671428571428571e-05,
      "loss": 3.5396,
      "step": 96
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.6678571428571435e-05,
      "loss": 3.4922,
      "step": 97
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.6642857142857144e-05,
      "loss": 3.3885,
      "step": 98
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.660714285714286e-05,
      "loss": 3.3618,
      "step": 99
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.6571428571428575e-05,
      "loss": 3.4719,
      "step": 100
    },
    {
      "epoch": 0.14,
      "eval_cer": 0.9611096363153703,
      "eval_loss": 3.239352226257324,
      "eval_runtime": 333.0578,
      "eval_samples_per_second": 0.7,
      "eval_steps_per_second": 0.351,
      "step": 100
    },
    {
      "epoch": 0.14,
      "learning_rate": 4.653571428571429e-05,
      "loss": 3.6861,
      "step": 101
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.6500000000000005e-05,
      "loss": 3.3363,
      "step": 102
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.6464285714285714e-05,
      "loss": 3.4917,
      "step": 103
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.642857142857143e-05,
      "loss": 4.1947,
      "step": 104
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.6392857142857145e-05,
      "loss": 3.5155,
      "step": 105
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.635714285714286e-05,
      "loss": 3.5659,
      "step": 106
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.632142857142857e-05,
      "loss": 3.7098,
      "step": 107
    },
    {
      "epoch": 0.15,
      "learning_rate": 4.628571428571429e-05,
      "loss": 3.4785,
      "step": 108
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.6250000000000006e-05,
      "loss": 3.5027,
      "step": 109
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.6214285714285715e-05,
      "loss": 3.3869,
      "step": 110
    },
    {
      "epoch": 0.16,
      "eval_cer": 0.9790284045659676,
      "eval_loss": 3.2285759449005127,
      "eval_runtime": 319.0089,
      "eval_samples_per_second": 0.73,
      "eval_steps_per_second": 0.367,
      "step": 110
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.617857142857143e-05,
      "loss": 3.2923,
      "step": 111
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.6142857142857145e-05,
      "loss": 3.4371,
      "step": 112
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.610714285714286e-05,
      "loss": 3.2465,
      "step": 113
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.607142857142857e-05,
      "loss": 3.3443,
      "step": 114
    },
    {
      "epoch": 0.16,
      "learning_rate": 4.6035714285714285e-05,
      "loss": 3.5028,
      "step": 115
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.600000000000001e-05,
      "loss": 3.557,
      "step": 116
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.5964285714285715e-05,
      "loss": 3.2903,
      "step": 117
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.592857142857143e-05,
      "loss": 3.236,
      "step": 118
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.5892857142857146e-05,
      "loss": 3.2228,
      "step": 119
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.585714285714286e-05,
      "loss": 3.1682,
      "step": 120
    },
    {
      "epoch": 0.17,
      "eval_cer": 0.964958853198832,
      "eval_loss": 3.1594746112823486,
      "eval_runtime": 324.5351,
      "eval_samples_per_second": 0.718,
      "eval_steps_per_second": 0.361,
      "step": 120
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.582142857142858e-05,
      "loss": 3.1485,
      "step": 121
    },
    {
      "epoch": 0.17,
      "learning_rate": 4.5785714285714285e-05,
      "loss": 3.3894,
      "step": 122
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.575e-05,
      "loss": 2.9311,
      "step": 123
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.5714285714285716e-05,
      "loss": 3.364,
      "step": 124
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.567857142857143e-05,
      "loss": 3.115,
      "step": 125
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.564285714285714e-05,
      "loss": 3.3045,
      "step": 126
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.560714285714286e-05,
      "loss": 3.0914,
      "step": 127
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.557142857142858e-05,
      "loss": 3.0347,
      "step": 128
    },
    {
      "epoch": 0.18,
      "learning_rate": 4.5535714285714286e-05,
      "loss": 3.2584,
      "step": 129
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.55e-05,
      "loss": 3.1872,
      "step": 130
    },
    {
      "epoch": 0.19,
      "eval_cer": 0.9891160074329706,
      "eval_loss": 3.1255040168762207,
      "eval_runtime": 323.0282,
      "eval_samples_per_second": 0.721,
      "eval_steps_per_second": 0.362,
      "step": 130
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.546428571428572e-05,
      "loss": 3.1836,
      "step": 131
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.542857142857143e-05,
      "loss": 3.4456,
      "step": 132
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.539285714285714e-05,
      "loss": 3.3621,
      "step": 133
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.5357142857142856e-05,
      "loss": 3.0413,
      "step": 134
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.532142857142858e-05,
      "loss": 3.026,
      "step": 135
    },
    {
      "epoch": 0.19,
      "learning_rate": 4.528571428571429e-05,
      "loss": 3.2816,
      "step": 136
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.525e-05,
      "loss": 3.089,
      "step": 137
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.521428571428572e-05,
      "loss": 3.0561,
      "step": 138
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.517857142857143e-05,
      "loss": 3.0419,
      "step": 139
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.514285714285714e-05,
      "loss": 3.1511,
      "step": 140
    },
    {
      "epoch": 0.2,
      "eval_cer": 0.9756437483408548,
      "eval_loss": 3.052809238433838,
      "eval_runtime": 323.3575,
      "eval_samples_per_second": 0.721,
      "eval_steps_per_second": 0.362,
      "step": 140
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.510714285714286e-05,
      "loss": 3.2687,
      "step": 141
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.507142857142858e-05,
      "loss": 3.023,
      "step": 142
    },
    {
      "epoch": 0.2,
      "learning_rate": 4.503571428571429e-05,
      "loss": 3.0185,
      "step": 143
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.5e-05,
      "loss": 3.0305,
      "step": 144
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.496428571428571e-05,
      "loss": 3.0141,
      "step": 145
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.4928571428571434e-05,
      "loss": 2.6496,
      "step": 146
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.489285714285715e-05,
      "loss": 3.255,
      "step": 147
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.485714285714286e-05,
      "loss": 3.5118,
      "step": 148
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.482142857142857e-05,
      "loss": 3.0693,
      "step": 149
    },
    {
      "epoch": 0.21,
      "learning_rate": 4.478571428571429e-05,
      "loss": 3.0689,
      "step": 150
    },
    {
      "epoch": 0.21,
      "eval_cer": 0.964958853198832,
      "eval_loss": 3.0696001052856445,
      "eval_runtime": 335.8658,
      "eval_samples_per_second": 0.694,
      "eval_steps_per_second": 0.348,
      "step": 150
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.4750000000000004e-05,
      "loss": 3.1652,
      "step": 151
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.471428571428571e-05,
      "loss": 3.205,
      "step": 152
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.467857142857143e-05,
      "loss": 2.936,
      "step": 153
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.464285714285715e-05,
      "loss": 3.1121,
      "step": 154
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.460714285714286e-05,
      "loss": 3.0119,
      "step": 155
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.4571428571428574e-05,
      "loss": 3.1201,
      "step": 156
    },
    {
      "epoch": 0.22,
      "learning_rate": 4.453571428571429e-05,
      "loss": 3.295,
      "step": 157
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.4500000000000004e-05,
      "loss": 3.1036,
      "step": 158
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.446428571428571e-05,
      "loss": 3.1456,
      "step": 159
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.442857142857143e-05,
      "loss": 3.0451,
      "step": 160
    },
    {
      "epoch": 0.23,
      "eval_cer": 0.9779001858242633,
      "eval_loss": 2.9864931106567383,
      "eval_runtime": 319.0636,
      "eval_samples_per_second": 0.73,
      "eval_steps_per_second": 0.367,
      "step": 160
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.439285714285715e-05,
      "loss": 3.2449,
      "step": 161
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.435714285714286e-05,
      "loss": 2.9592,
      "step": 162
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.4321428571428574e-05,
      "loss": 3.0033,
      "step": 163
    },
    {
      "epoch": 0.23,
      "learning_rate": 4.428571428571428e-05,
      "loss": 2.9914,
      "step": 164
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.4250000000000005e-05,
      "loss": 3.1761,
      "step": 165
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.4214285714285714e-05,
      "loss": 3.1854,
      "step": 166
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.417857142857143e-05,
      "loss": 2.9826,
      "step": 167
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.4142857142857144e-05,
      "loss": 3.1795,
      "step": 168
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.410714285714286e-05,
      "loss": 2.8349,
      "step": 169
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.4071428571428575e-05,
      "loss": 2.9363,
      "step": 170
    },
    {
      "epoch": 0.24,
      "eval_cer": 0.9589195646402974,
      "eval_loss": 3.021003484725952,
      "eval_runtime": 317.9632,
      "eval_samples_per_second": 0.733,
      "eval_steps_per_second": 0.368,
      "step": 170
    },
    {
      "epoch": 0.24,
      "learning_rate": 4.4035714285714284e-05,
      "loss": 3.3417,
      "step": 171
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.4000000000000006e-05,
      "loss": 2.9261,
      "step": 172
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.396428571428572e-05,
      "loss": 2.9945,
      "step": 173
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.392857142857143e-05,
      "loss": 3.2001,
      "step": 174
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.3892857142857145e-05,
      "loss": 3.5838,
      "step": 175
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.385714285714286e-05,
      "loss": 2.9582,
      "step": 176
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.3821428571428576e-05,
      "loss": 2.9543,
      "step": 177
    },
    {
      "epoch": 0.25,
      "learning_rate": 4.3785714285714284e-05,
      "loss": 3.4312,
      "step": 178
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.375e-05,
      "loss": 3.2692,
      "step": 179
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.371428571428572e-05,
      "loss": 3.0356,
      "step": 180
    },
    {
      "epoch": 0.26,
      "eval_cer": 0.9732545792407752,
      "eval_loss": 2.9228129386901855,
      "eval_runtime": 320.4691,
      "eval_samples_per_second": 0.727,
      "eval_steps_per_second": 0.365,
      "step": 180
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.367857142857143e-05,
      "loss": 3.0399,
      "step": 181
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.3642857142857146e-05,
      "loss": 3.1621,
      "step": 182
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.3607142857142854e-05,
      "loss": 2.8064,
      "step": 183
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.3571428571428576e-05,
      "loss": 3.6683,
      "step": 184
    },
    {
      "epoch": 0.26,
      "learning_rate": 4.3535714285714285e-05,
      "loss": 2.9462,
      "step": 185
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.35e-05,
      "loss": 3.2146,
      "step": 186
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.3464285714285716e-05,
      "loss": 2.8593,
      "step": 187
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.342857142857143e-05,
      "loss": 2.9732,
      "step": 188
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.3392857142857146e-05,
      "loss": 2.9865,
      "step": 189
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.3357142857142855e-05,
      "loss": 2.9325,
      "step": 190
    },
    {
      "epoch": 0.27,
      "eval_cer": 0.9613750995487125,
      "eval_loss": 2.922090530395508,
      "eval_runtime": 311.5106,
      "eval_samples_per_second": 0.748,
      "eval_steps_per_second": 0.376,
      "step": 190
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.332142857142858e-05,
      "loss": 3.0196,
      "step": 191
    },
    {
      "epoch": 0.27,
      "learning_rate": 4.328571428571429e-05,
      "loss": 3.0039,
      "step": 192
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.325e-05,
      "loss": 3.1287,
      "step": 193
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.3214285714285716e-05,
      "loss": 2.8974,
      "step": 194
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.317857142857143e-05,
      "loss": 3.128,
      "step": 195
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.314285714285715e-05,
      "loss": 3.5584,
      "step": 196
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.3107142857142856e-05,
      "loss": 3.1332,
      "step": 197
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.307142857142857e-05,
      "loss": 2.8884,
      "step": 198
    },
    {
      "epoch": 0.28,
      "learning_rate": 4.303571428571429e-05,
      "loss": 3.0141,
      "step": 199
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.3e-05,
      "loss": 2.9832,
      "step": 200
    },
    {
      "epoch": 0.29,
      "eval_cer": 0.9861959118662065,
      "eval_loss": 2.8819756507873535,
      "eval_runtime": 314.3527,
      "eval_samples_per_second": 0.741,
      "eval_steps_per_second": 0.372,
      "step": 200
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.296428571428572e-05,
      "loss": 2.9334,
      "step": 201
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.292857142857143e-05,
      "loss": 3.2626,
      "step": 202
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.289285714285715e-05,
      "loss": 2.937,
      "step": 203
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.2857142857142856e-05,
      "loss": 3.1081,
      "step": 204
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.282142857142857e-05,
      "loss": 3.4302,
      "step": 205
    },
    {
      "epoch": 0.29,
      "learning_rate": 4.278571428571429e-05,
      "loss": 2.9269,
      "step": 206
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.275e-05,
      "loss": 2.8063,
      "step": 207
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.271428571428572e-05,
      "loss": 3.0449,
      "step": 208
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.2678571428571426e-05,
      "loss": 2.9923,
      "step": 209
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.264285714285715e-05,
      "loss": 2.7053,
      "step": 210
    },
    {
      "epoch": 0.3,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.840769052505493,
      "eval_runtime": 323.1103,
      "eval_samples_per_second": 0.721,
      "eval_steps_per_second": 0.362,
      "step": 210
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.260714285714286e-05,
      "loss": 2.8218,
      "step": 211
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.257142857142857e-05,
      "loss": 3.2829,
      "step": 212
    },
    {
      "epoch": 0.3,
      "learning_rate": 4.253571428571429e-05,
      "loss": 3.0546,
      "step": 213
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.25e-05,
      "loss": 2.7331,
      "step": 214
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.246428571428572e-05,
      "loss": 2.9502,
      "step": 215
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.242857142857143e-05,
      "loss": 2.9325,
      "step": 216
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.239285714285714e-05,
      "loss": 3.0527,
      "step": 217
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.2357142857142864e-05,
      "loss": 2.9817,
      "step": 218
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.232142857142857e-05,
      "loss": 3.106,
      "step": 219
    },
    {
      "epoch": 0.31,
      "learning_rate": 4.228571428571429e-05,
      "loss": 2.6862,
      "step": 220
    },
    {
      "epoch": 0.31,
      "eval_cer": 0.9738518715157951,
      "eval_loss": 2.838029384613037,
      "eval_runtime": 328.277,
      "eval_samples_per_second": 0.71,
      "eval_steps_per_second": 0.356,
      "step": 220
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.2250000000000004e-05,
      "loss": 2.9462,
      "step": 221
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.221428571428572e-05,
      "loss": 2.9561,
      "step": 222
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.217857142857143e-05,
      "loss": 3.0025,
      "step": 223
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.214285714285714e-05,
      "loss": 2.7712,
      "step": 224
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.210714285714286e-05,
      "loss": 3.0134,
      "step": 225
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.2071428571428574e-05,
      "loss": 3.0482,
      "step": 226
    },
    {
      "epoch": 0.32,
      "learning_rate": 4.203571428571429e-05,
      "loss": 2.8388,
      "step": 227
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.2e-05,
      "loss": 2.8731,
      "step": 228
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.196428571428572e-05,
      "loss": 2.9786,
      "step": 229
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.192857142857143e-05,
      "loss": 3.0149,
      "step": 230
    },
    {
      "epoch": 0.33,
      "eval_cer": 0.9742500663658084,
      "eval_loss": 2.832563877105713,
      "eval_runtime": 316.7831,
      "eval_samples_per_second": 0.736,
      "eval_steps_per_second": 0.369,
      "step": 230
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.1892857142857144e-05,
      "loss": 2.8631,
      "step": 231
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.185714285714286e-05,
      "loss": 2.7531,
      "step": 232
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.1821428571428574e-05,
      "loss": 2.8076,
      "step": 233
    },
    {
      "epoch": 0.33,
      "learning_rate": 4.178571428571429e-05,
      "loss": 3.153,
      "step": 234
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.175e-05,
      "loss": 2.7963,
      "step": 235
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.1714285714285714e-05,
      "loss": 2.7109,
      "step": 236
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.167857142857143e-05,
      "loss": 3.0023,
      "step": 237
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.1642857142857144e-05,
      "loss": 2.8564,
      "step": 238
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.160714285714286e-05,
      "loss": 2.7772,
      "step": 239
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.1571428571428575e-05,
      "loss": 2.9958,
      "step": 240
    },
    {
      "epoch": 0.34,
      "eval_cer": 0.9654897796655163,
      "eval_loss": 2.8167169094085693,
      "eval_runtime": 318.6014,
      "eval_samples_per_second": 0.731,
      "eval_steps_per_second": 0.367,
      "step": 240
    },
    {
      "epoch": 0.34,
      "learning_rate": 4.153571428571429e-05,
      "loss": 2.6758,
      "step": 241
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.15e-05,
      "loss": 2.7747,
      "step": 242
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.1464285714285714e-05,
      "loss": 2.8545,
      "step": 243
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.1428571428571437e-05,
      "loss": 2.7938,
      "step": 244
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.1392857142857145e-05,
      "loss": 2.6511,
      "step": 245
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.135714285714286e-05,
      "loss": 3.0812,
      "step": 246
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.132142857142857e-05,
      "loss": 2.7769,
      "step": 247
    },
    {
      "epoch": 0.35,
      "learning_rate": 4.128571428571429e-05,
      "loss": 2.686,
      "step": 248
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.125e-05,
      "loss": 4.2661,
      "step": 249
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.1214285714285715e-05,
      "loss": 2.9914,
      "step": 250
    },
    {
      "epoch": 0.36,
      "eval_cer": 0.9741837005574728,
      "eval_loss": 2.807875394821167,
      "eval_runtime": 321.598,
      "eval_samples_per_second": 0.725,
      "eval_steps_per_second": 0.364,
      "step": 250
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.117857142857143e-05,
      "loss": 2.7861,
      "step": 251
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.1142857142857146e-05,
      "loss": 2.7627,
      "step": 252
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.110714285714286e-05,
      "loss": 2.6929,
      "step": 253
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.107142857142857e-05,
      "loss": 2.851,
      "step": 254
    },
    {
      "epoch": 0.36,
      "learning_rate": 4.1035714285714285e-05,
      "loss": 3.0091,
      "step": 255
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.1e-05,
      "loss": 2.9892,
      "step": 256
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.0964285714285716e-05,
      "loss": 2.8118,
      "step": 257
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.092857142857143e-05,
      "loss": 2.7554,
      "step": 258
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.0892857142857147e-05,
      "loss": 2.9773,
      "step": 259
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.085714285714286e-05,
      "loss": 2.6739,
      "step": 260
    },
    {
      "epoch": 0.37,
      "eval_cer": 0.9589195646402974,
      "eval_loss": 2.7577922344207764,
      "eval_runtime": 319.0337,
      "eval_samples_per_second": 0.73,
      "eval_steps_per_second": 0.367,
      "step": 260
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.082142857142857e-05,
      "loss": 2.6573,
      "step": 261
    },
    {
      "epoch": 0.37,
      "learning_rate": 4.0785714285714286e-05,
      "loss": 3.1113,
      "step": 262
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.075e-05,
      "loss": 3.4335,
      "step": 263
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.0714285714285717e-05,
      "loss": 2.7478,
      "step": 264
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.067857142857143e-05,
      "loss": 2.8522,
      "step": 265
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.064285714285714e-05,
      "loss": 2.8707,
      "step": 266
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.060714285714286e-05,
      "loss": 3.0285,
      "step": 267
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.057142857142857e-05,
      "loss": 2.8029,
      "step": 268
    },
    {
      "epoch": 0.38,
      "learning_rate": 4.0535714285714287e-05,
      "loss": 2.9584,
      "step": 269
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.05e-05,
      "loss": 2.8299,
      "step": 270
    },
    {
      "epoch": 0.39,
      "eval_cer": 0.961308733740377,
      "eval_loss": 2.7699763774871826,
      "eval_runtime": 323.9191,
      "eval_samples_per_second": 0.719,
      "eval_steps_per_second": 0.361,
      "step": 270
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.046428571428572e-05,
      "loss": 2.8539,
      "step": 271
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.042857142857143e-05,
      "loss": 3.004,
      "step": 272
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.039285714285714e-05,
      "loss": 2.9303,
      "step": 273
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.035714285714286e-05,
      "loss": 2.7056,
      "step": 274
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.032142857142857e-05,
      "loss": 2.8193,
      "step": 275
    },
    {
      "epoch": 0.39,
      "learning_rate": 4.028571428571429e-05,
      "loss": 2.7011,
      "step": 276
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.025e-05,
      "loss": 2.8853,
      "step": 277
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.021428571428572e-05,
      "loss": 2.9468,
      "step": 278
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.017857142857143e-05,
      "loss": 3.0224,
      "step": 279
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.014285714285714e-05,
      "loss": 2.5312,
      "step": 280
    },
    {
      "epoch": 0.4,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.7938787937164307,
      "eval_runtime": 314.2808,
      "eval_samples_per_second": 0.741,
      "eval_steps_per_second": 0.372,
      "step": 280
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.010714285714286e-05,
      "loss": 2.8237,
      "step": 281
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.007142857142857e-05,
      "loss": 3.0713,
      "step": 282
    },
    {
      "epoch": 0.4,
      "learning_rate": 4.003571428571429e-05,
      "loss": 2.7787,
      "step": 283
    },
    {
      "epoch": 0.41,
      "learning_rate": 4e-05,
      "loss": 2.8789,
      "step": 284
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.996428571428571e-05,
      "loss": 2.6393,
      "step": 285
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.9928571428571434e-05,
      "loss": 2.7942,
      "step": 286
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.989285714285714e-05,
      "loss": 2.9031,
      "step": 287
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.985714285714286e-05,
      "loss": 2.8729,
      "step": 288
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.982142857142857e-05,
      "loss": 2.9101,
      "step": 289
    },
    {
      "epoch": 0.41,
      "learning_rate": 3.978571428571429e-05,
      "loss": 2.7669,
      "step": 290
    },
    {
      "epoch": 0.41,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.7678186893463135,
      "eval_runtime": 315.4699,
      "eval_samples_per_second": 0.739,
      "eval_steps_per_second": 0.371,
      "step": 290
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.9750000000000004e-05,
      "loss": 2.8024,
      "step": 291
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.971428571428571e-05,
      "loss": 2.6509,
      "step": 292
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.9678571428571435e-05,
      "loss": 2.7236,
      "step": 293
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.964285714285714e-05,
      "loss": 2.815,
      "step": 294
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.960714285714286e-05,
      "loss": 2.7654,
      "step": 295
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.9571428571428574e-05,
      "loss": 2.7474,
      "step": 296
    },
    {
      "epoch": 0.42,
      "learning_rate": 3.953571428571429e-05,
      "loss": 2.5751,
      "step": 297
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.9500000000000005e-05,
      "loss": 2.5654,
      "step": 298
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.946428571428571e-05,
      "loss": 2.8024,
      "step": 299
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.942857142857143e-05,
      "loss": 3.145,
      "step": 300
    },
    {
      "epoch": 0.43,
      "eval_cer": 0.9592513936819751,
      "eval_loss": 2.8047523498535156,
      "eval_runtime": 316.9525,
      "eval_samples_per_second": 0.735,
      "eval_steps_per_second": 0.369,
      "step": 300
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.9392857142857144e-05,
      "loss": 2.7441,
      "step": 301
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.935714285714286e-05,
      "loss": 3.0497,
      "step": 302
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.9321428571428575e-05,
      "loss": 2.5291,
      "step": 303
    },
    {
      "epoch": 0.43,
      "learning_rate": 3.928571428571429e-05,
      "loss": 2.6084,
      "step": 304
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.9250000000000005e-05,
      "loss": 2.8092,
      "step": 305
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.9214285714285714e-05,
      "loss": 3.1391,
      "step": 306
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.917857142857143e-05,
      "loss": 2.7074,
      "step": 307
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.9142857142857145e-05,
      "loss": 2.7903,
      "step": 308
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.910714285714286e-05,
      "loss": 2.8339,
      "step": 309
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.9071428571428575e-05,
      "loss": 2.6182,
      "step": 310
    },
    {
      "epoch": 0.44,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.731799840927124,
      "eval_runtime": 316.9198,
      "eval_samples_per_second": 0.735,
      "eval_steps_per_second": 0.369,
      "step": 310
    },
    {
      "epoch": 0.44,
      "learning_rate": 3.9035714285714284e-05,
      "loss": 2.7583,
      "step": 311
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.9000000000000006e-05,
      "loss": 2.9672,
      "step": 312
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.8964285714285715e-05,
      "loss": 2.9053,
      "step": 313
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.892857142857143e-05,
      "loss": 2.8132,
      "step": 314
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.8892857142857145e-05,
      "loss": 2.7611,
      "step": 315
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.885714285714286e-05,
      "loss": 2.7535,
      "step": 316
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.8821428571428576e-05,
      "loss": 2.9038,
      "step": 317
    },
    {
      "epoch": 0.45,
      "learning_rate": 3.8785714285714285e-05,
      "loss": 2.885,
      "step": 318
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.875e-05,
      "loss": 2.6586,
      "step": 319
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.8714285714285715e-05,
      "loss": 2.818,
      "step": 320
    },
    {
      "epoch": 0.46,
      "eval_cer": 0.9609105388903637,
      "eval_loss": 2.7775094509124756,
      "eval_runtime": 309.6249,
      "eval_samples_per_second": 0.753,
      "eval_steps_per_second": 0.378,
      "step": 320
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.867857142857143e-05,
      "loss": 2.8653,
      "step": 321
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.8642857142857146e-05,
      "loss": 3.0002,
      "step": 322
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.860714285714286e-05,
      "loss": 2.669,
      "step": 323
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.857142857142858e-05,
      "loss": 2.8644,
      "step": 324
    },
    {
      "epoch": 0.46,
      "learning_rate": 3.8535714285714285e-05,
      "loss": 2.97,
      "step": 325
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.85e-05,
      "loss": 2.9073,
      "step": 326
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.8464285714285716e-05,
      "loss": 2.7792,
      "step": 327
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.842857142857143e-05,
      "loss": 2.5836,
      "step": 328
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.839285714285715e-05,
      "loss": 2.8181,
      "step": 329
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.8357142857142855e-05,
      "loss": 2.8184,
      "step": 330
    },
    {
      "epoch": 0.47,
      "eval_cer": 0.9607778072736926,
      "eval_loss": 2.709090232849121,
      "eval_runtime": 313.6079,
      "eval_samples_per_second": 0.743,
      "eval_steps_per_second": 0.373,
      "step": 330
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.832142857142858e-05,
      "loss": 2.9264,
      "step": 331
    },
    {
      "epoch": 0.47,
      "learning_rate": 3.8285714285714286e-05,
      "loss": 3.0099,
      "step": 332
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.825e-05,
      "loss": 2.6006,
      "step": 333
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.821428571428572e-05,
      "loss": 2.8656,
      "step": 334
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.817857142857143e-05,
      "loss": 2.742,
      "step": 335
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.814285714285715e-05,
      "loss": 2.5418,
      "step": 336
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.8107142857142856e-05,
      "loss": 2.6411,
      "step": 337
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.807142857142857e-05,
      "loss": 2.8933,
      "step": 338
    },
    {
      "epoch": 0.48,
      "learning_rate": 3.803571428571429e-05,
      "loss": 2.7295,
      "step": 339
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.8e-05,
      "loss": 2.7025,
      "step": 340
    },
    {
      "epoch": 0.49,
      "eval_cer": 0.9589195646402974,
      "eval_loss": 2.6730380058288574,
      "eval_runtime": 317.7953,
      "eval_samples_per_second": 0.733,
      "eval_steps_per_second": 0.368,
      "step": 340
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.796428571428571e-05,
      "loss": 2.5152,
      "step": 341
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.792857142857143e-05,
      "loss": 2.7111,
      "step": 342
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.789285714285715e-05,
      "loss": 2.9314,
      "step": 343
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.785714285714286e-05,
      "loss": 3.0277,
      "step": 344
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.782142857142857e-05,
      "loss": 2.5198,
      "step": 345
    },
    {
      "epoch": 0.49,
      "learning_rate": 3.778571428571429e-05,
      "loss": 2.7188,
      "step": 346
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.775e-05,
      "loss": 2.6115,
      "step": 347
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.771428571428572e-05,
      "loss": 2.651,
      "step": 348
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.767857142857143e-05,
      "loss": 2.6941,
      "step": 349
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.764285714285715e-05,
      "loss": 2.5636,
      "step": 350
    },
    {
      "epoch": 0.5,
      "eval_cer": 0.9613750995487125,
      "eval_loss": 2.7367913722991943,
      "eval_runtime": 315.5862,
      "eval_samples_per_second": 0.738,
      "eval_steps_per_second": 0.371,
      "step": 350
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.760714285714286e-05,
      "loss": 2.886,
      "step": 351
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.757142857142857e-05,
      "loss": 3.0787,
      "step": 352
    },
    {
      "epoch": 0.5,
      "learning_rate": 3.753571428571429e-05,
      "loss": 2.6632,
      "step": 353
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.7500000000000003e-05,
      "loss": 2.9465,
      "step": 354
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.746428571428572e-05,
      "loss": 2.7208,
      "step": 355
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.742857142857143e-05,
      "loss": 2.8653,
      "step": 356
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.739285714285714e-05,
      "loss": 2.7124,
      "step": 357
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.735714285714286e-05,
      "loss": 2.8303,
      "step": 358
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.7321428571428573e-05,
      "loss": 2.754,
      "step": 359
    },
    {
      "epoch": 0.51,
      "learning_rate": 3.728571428571428e-05,
      "loss": 2.7938,
      "step": 360
    },
    {
      "epoch": 0.51,
      "eval_cer": 0.991239713299708,
      "eval_loss": 2.7412941455841064,
      "eval_runtime": 318.2026,
      "eval_samples_per_second": 0.732,
      "eval_steps_per_second": 0.368,
      "step": 360
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.7250000000000004e-05,
      "loss": 2.6228,
      "step": 361
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.721428571428572e-05,
      "loss": 2.7221,
      "step": 362
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.717857142857143e-05,
      "loss": 2.8257,
      "step": 363
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.7142857142857143e-05,
      "loss": 2.8805,
      "step": 364
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.710714285714286e-05,
      "loss": 2.8008,
      "step": 365
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.7071428571428574e-05,
      "loss": 2.7788,
      "step": 366
    },
    {
      "epoch": 0.52,
      "learning_rate": 3.703571428571429e-05,
      "loss": 2.771,
      "step": 367
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.7e-05,
      "loss": 2.7131,
      "step": 368
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.696428571428572e-05,
      "loss": 2.6139,
      "step": 369
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.692857142857143e-05,
      "loss": 2.5876,
      "step": 370
    },
    {
      "epoch": 0.53,
      "eval_cer": 0.97809928324927,
      "eval_loss": 2.671900987625122,
      "eval_runtime": 326.1883,
      "eval_samples_per_second": 0.714,
      "eval_steps_per_second": 0.359,
      "step": 370
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.6892857142857144e-05,
      "loss": 2.5711,
      "step": 371
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.685714285714286e-05,
      "loss": 2.646,
      "step": 372
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.6821428571428575e-05,
      "loss": 2.7535,
      "step": 373
    },
    {
      "epoch": 0.53,
      "learning_rate": 3.678571428571429e-05,
      "loss": 2.707,
      "step": 374
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.675e-05,
      "loss": 2.7198,
      "step": 375
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.671428571428572e-05,
      "loss": 2.7891,
      "step": 376
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.667857142857143e-05,
      "loss": 2.806,
      "step": 377
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.6642857142857145e-05,
      "loss": 2.7419,
      "step": 378
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.6607142857142853e-05,
      "loss": 2.5651,
      "step": 379
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.6571428571428576e-05,
      "loss": 2.771,
      "step": 380
    },
    {
      "epoch": 0.54,
      "eval_cer": 0.977369259357579,
      "eval_loss": 2.6480963230133057,
      "eval_runtime": 316.9664,
      "eval_samples_per_second": 0.735,
      "eval_steps_per_second": 0.369,
      "step": 380
    },
    {
      "epoch": 0.54,
      "learning_rate": 3.653571428571429e-05,
      "loss": 2.7975,
      "step": 381
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.65e-05,
      "loss": 2.8994,
      "step": 382
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.6464285714285715e-05,
      "loss": 2.5236,
      "step": 383
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.642857142857143e-05,
      "loss": 2.7253,
      "step": 384
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.6392857142857146e-05,
      "loss": 2.654,
      "step": 385
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.6357142857142854e-05,
      "loss": 2.8336,
      "step": 386
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.6321428571428576e-05,
      "loss": 2.7935,
      "step": 387
    },
    {
      "epoch": 0.55,
      "learning_rate": 3.628571428571429e-05,
      "loss": 2.7351,
      "step": 388
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.625e-05,
      "loss": 2.7241,
      "step": 389
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.6214285714285716e-05,
      "loss": 2.8377,
      "step": 390
    },
    {
      "epoch": 0.56,
      "eval_cer": 0.9755773825325192,
      "eval_loss": 2.6397407054901123,
      "eval_runtime": 320.6012,
      "eval_samples_per_second": 0.727,
      "eval_steps_per_second": 0.365,
      "step": 390
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.617857142857143e-05,
      "loss": 2.5886,
      "step": 391
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.6142857142857146e-05,
      "loss": 2.6938,
      "step": 392
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.610714285714286e-05,
      "loss": 2.6291,
      "step": 393
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.607142857142857e-05,
      "loss": 3.1911,
      "step": 394
    },
    {
      "epoch": 0.56,
      "learning_rate": 3.603571428571429e-05,
      "loss": 2.9198,
      "step": 395
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.6e-05,
      "loss": 2.7068,
      "step": 396
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.5964285714285716e-05,
      "loss": 2.6928,
      "step": 397
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.5928571428571425e-05,
      "loss": 2.701,
      "step": 398
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.589285714285715e-05,
      "loss": 2.6824,
      "step": 399
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.585714285714286e-05,
      "loss": 2.8384,
      "step": 400
    },
    {
      "epoch": 0.57,
      "eval_cer": 0.9644942925404831,
      "eval_loss": 2.7028393745422363,
      "eval_runtime": 287.3344,
      "eval_samples_per_second": 0.811,
      "eval_steps_per_second": 0.407,
      "step": 400
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.582142857142857e-05,
      "loss": 2.843,
      "step": 401
    },
    {
      "epoch": 0.57,
      "learning_rate": 3.5785714285714286e-05,
      "loss": 2.6555,
      "step": 402
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.575e-05,
      "loss": 2.8313,
      "step": 403
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.571428571428572e-05,
      "loss": 2.6572,
      "step": 404
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.5678571428571426e-05,
      "loss": 2.7201,
      "step": 405
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.564285714285715e-05,
      "loss": 2.6196,
      "step": 406
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.560714285714286e-05,
      "loss": 2.6819,
      "step": 407
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.557142857142857e-05,
      "loss": 2.601,
      "step": 408
    },
    {
      "epoch": 0.58,
      "learning_rate": 3.553571428571429e-05,
      "loss": 3.1449,
      "step": 409
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.55e-05,
      "loss": 2.5814,
      "step": 410
    },
    {
      "epoch": 0.59,
      "eval_cer": 0.9740509689408017,
      "eval_loss": 2.6410415172576904,
      "eval_runtime": 74.1913,
      "eval_samples_per_second": 3.141,
      "eval_steps_per_second": 1.577,
      "step": 410
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.546428571428572e-05,
      "loss": 3.2745,
      "step": 411
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.5428571428571426e-05,
      "loss": 2.6258,
      "step": 412
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.539285714285714e-05,
      "loss": 2.7162,
      "step": 413
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.5357142857142864e-05,
      "loss": 2.5559,
      "step": 414
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.532142857142857e-05,
      "loss": 2.8926,
      "step": 415
    },
    {
      "epoch": 0.59,
      "learning_rate": 3.528571428571429e-05,
      "loss": 2.7433,
      "step": 416
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.525e-05,
      "loss": 2.7035,
      "step": 417
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.521428571428572e-05,
      "loss": 2.5861,
      "step": 418
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.5178571428571434e-05,
      "loss": 2.6221,
      "step": 419
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.514285714285714e-05,
      "loss": 2.6132,
      "step": 420
    },
    {
      "epoch": 0.6,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.6286871433258057,
      "eval_runtime": 75.4509,
      "eval_samples_per_second": 3.088,
      "eval_steps_per_second": 1.551,
      "step": 420
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.510714285714286e-05,
      "loss": 2.7239,
      "step": 421
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.507142857142857e-05,
      "loss": 2.6661,
      "step": 422
    },
    {
      "epoch": 0.6,
      "learning_rate": 3.503571428571429e-05,
      "loss": 2.5105,
      "step": 423
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.5e-05,
      "loss": 2.4333,
      "step": 424
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.496428571428572e-05,
      "loss": 2.5897,
      "step": 425
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.4928571428571434e-05,
      "loss": 2.7033,
      "step": 426
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.489285714285714e-05,
      "loss": 2.6465,
      "step": 427
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.485714285714286e-05,
      "loss": 2.5459,
      "step": 428
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.4821428571428574e-05,
      "loss": 2.5863,
      "step": 429
    },
    {
      "epoch": 0.61,
      "learning_rate": 3.478571428571429e-05,
      "loss": 2.6991,
      "step": 430
    },
    {
      "epoch": 0.61,
      "eval_cer": 0.9744491637908149,
      "eval_loss": 2.673091173171997,
      "eval_runtime": 72.5187,
      "eval_samples_per_second": 3.213,
      "eval_steps_per_second": 1.613,
      "step": 430
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.475e-05,
      "loss": 2.6555,
      "step": 431
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.471428571428571e-05,
      "loss": 2.7849,
      "step": 432
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.4678571428571435e-05,
      "loss": 2.4486,
      "step": 433
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.4642857142857144e-05,
      "loss": 2.7173,
      "step": 434
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.460714285714286e-05,
      "loss": 3.0484,
      "step": 435
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.4571428571428574e-05,
      "loss": 2.716,
      "step": 436
    },
    {
      "epoch": 0.62,
      "learning_rate": 3.453571428571429e-05,
      "loss": 2.6721,
      "step": 437
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.45e-05,
      "loss": 2.9913,
      "step": 438
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.4464285714285714e-05,
      "loss": 2.6441,
      "step": 439
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.442857142857143e-05,
      "loss": 2.7615,
      "step": 440
    },
    {
      "epoch": 0.63,
      "eval_cer": 0.9680780461906026,
      "eval_loss": 2.631340503692627,
      "eval_runtime": 71.4348,
      "eval_samples_per_second": 3.262,
      "eval_steps_per_second": 1.638,
      "step": 440
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.4392857142857144e-05,
      "loss": 2.5436,
      "step": 441
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.435714285714286e-05,
      "loss": 2.5954,
      "step": 442
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.432142857142857e-05,
      "loss": 2.5975,
      "step": 443
    },
    {
      "epoch": 0.63,
      "learning_rate": 3.428571428571429e-05,
      "loss": 2.8386,
      "step": 444
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.4250000000000006e-05,
      "loss": 2.5975,
      "step": 445
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.4214285714285714e-05,
      "loss": 2.6041,
      "step": 446
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.417857142857143e-05,
      "loss": 2.7345,
      "step": 447
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.4142857142857145e-05,
      "loss": 2.5695,
      "step": 448
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.410714285714286e-05,
      "loss": 2.721,
      "step": 449
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.407142857142857e-05,
      "loss": 2.8635,
      "step": 450
    },
    {
      "epoch": 0.64,
      "eval_cer": 0.9611096363153703,
      "eval_loss": 2.5789968967437744,
      "eval_runtime": 71.3234,
      "eval_samples_per_second": 3.267,
      "eval_steps_per_second": 1.64,
      "step": 450
    },
    {
      "epoch": 0.64,
      "learning_rate": 3.4035714285714284e-05,
      "loss": 2.7303,
      "step": 451
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.4000000000000007e-05,
      "loss": 2.5009,
      "step": 452
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.3964285714285715e-05,
      "loss": 2.8082,
      "step": 453
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.392857142857143e-05,
      "loss": 2.6291,
      "step": 454
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.3892857142857146e-05,
      "loss": 2.5336,
      "step": 455
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.385714285714286e-05,
      "loss": 2.7766,
      "step": 456
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.382142857142857e-05,
      "loss": 2.8017,
      "step": 457
    },
    {
      "epoch": 0.65,
      "learning_rate": 3.3785714285714285e-05,
      "loss": 2.5643,
      "step": 458
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.375000000000001e-05,
      "loss": 2.48,
      "step": 459
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.3714285714285716e-05,
      "loss": 2.8466,
      "step": 460
    },
    {
      "epoch": 0.66,
      "eval_cer": 0.9727900185824263,
      "eval_loss": 2.583423376083374,
      "eval_runtime": 72.3675,
      "eval_samples_per_second": 3.22,
      "eval_steps_per_second": 1.617,
      "step": 460
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.367857142857143e-05,
      "loss": 2.9116,
      "step": 461
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.364285714285714e-05,
      "loss": 2.6382,
      "step": 462
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.360714285714286e-05,
      "loss": 2.7111,
      "step": 463
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.357142857142857e-05,
      "loss": 2.6515,
      "step": 464
    },
    {
      "epoch": 0.66,
      "learning_rate": 3.3535714285714286e-05,
      "loss": 2.6474,
      "step": 465
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.35e-05,
      "loss": 2.5784,
      "step": 466
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.3464285714285716e-05,
      "loss": 2.5309,
      "step": 467
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.342857142857143e-05,
      "loss": 2.6444,
      "step": 468
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.339285714285714e-05,
      "loss": 2.5995,
      "step": 469
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.3357142857142856e-05,
      "loss": 2.74,
      "step": 470
    },
    {
      "epoch": 0.67,
      "eval_cer": 0.9738518715157951,
      "eval_loss": 2.566138982772827,
      "eval_runtime": 72.5257,
      "eval_samples_per_second": 3.213,
      "eval_steps_per_second": 1.613,
      "step": 470
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.332142857142858e-05,
      "loss": 2.5212,
      "step": 471
    },
    {
      "epoch": 0.67,
      "learning_rate": 3.3285714285714286e-05,
      "loss": 2.5794,
      "step": 472
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.325e-05,
      "loss": 2.9375,
      "step": 473
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.321428571428572e-05,
      "loss": 2.6878,
      "step": 474
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.317857142857143e-05,
      "loss": 2.5704,
      "step": 475
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.314285714285714e-05,
      "loss": 2.6127,
      "step": 476
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.3107142857142856e-05,
      "loss": 3.084,
      "step": 477
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.307142857142858e-05,
      "loss": 2.8535,
      "step": 478
    },
    {
      "epoch": 0.68,
      "learning_rate": 3.303571428571429e-05,
      "loss": 2.6599,
      "step": 479
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.3e-05,
      "loss": 2.6452,
      "step": 480
    },
    {
      "epoch": 0.69,
      "eval_cer": 0.97809928324927,
      "eval_loss": 2.598479747772217,
      "eval_runtime": 73.2128,
      "eval_samples_per_second": 3.183,
      "eval_steps_per_second": 1.598,
      "step": 480
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.296428571428571e-05,
      "loss": 2.9095,
      "step": 481
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.292857142857143e-05,
      "loss": 2.6337,
      "step": 482
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.289285714285714e-05,
      "loss": 2.6865,
      "step": 483
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.285714285714286e-05,
      "loss": 2.7893,
      "step": 484
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.282142857142857e-05,
      "loss": 2.2989,
      "step": 485
    },
    {
      "epoch": 0.69,
      "learning_rate": 3.278571428571429e-05,
      "loss": 2.609,
      "step": 486
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.275e-05,
      "loss": 2.4387,
      "step": 487
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.271428571428571e-05,
      "loss": 2.8439,
      "step": 488
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.2678571428571434e-05,
      "loss": 2.6816,
      "step": 489
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.264285714285714e-05,
      "loss": 2.6967,
      "step": 490
    },
    {
      "epoch": 0.7,
      "eval_cer": 0.9727236527740908,
      "eval_loss": 2.569263219833374,
      "eval_runtime": 77.6434,
      "eval_samples_per_second": 3.001,
      "eval_steps_per_second": 1.507,
      "step": 490
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.260714285714286e-05,
      "loss": 2.5323,
      "step": 491
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.257142857142857e-05,
      "loss": 2.656,
      "step": 492
    },
    {
      "epoch": 0.7,
      "learning_rate": 3.253571428571429e-05,
      "loss": 2.2834,
      "step": 493
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.2500000000000004e-05,
      "loss": 2.6888,
      "step": 494
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.246428571428571e-05,
      "loss": 2.5444,
      "step": 495
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.242857142857143e-05,
      "loss": 2.6781,
      "step": 496
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.239285714285715e-05,
      "loss": 2.6016,
      "step": 497
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.235714285714286e-05,
      "loss": 2.5921,
      "step": 498
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.2321428571428574e-05,
      "loss": 2.595,
      "step": 499
    },
    {
      "epoch": 0.71,
      "learning_rate": 3.228571428571428e-05,
      "loss": 2.5341,
      "step": 500
    },
    {
      "epoch": 0.71,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.5395655632019043,
      "eval_runtime": 72.6066,
      "eval_samples_per_second": 3.209,
      "eval_steps_per_second": 1.611,
      "step": 500
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.2250000000000005e-05,
      "loss": 2.8666,
      "step": 501
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.221428571428571e-05,
      "loss": 2.3849,
      "step": 502
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.217857142857143e-05,
      "loss": 2.6348,
      "step": 503
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.2142857142857144e-05,
      "loss": 2.8089,
      "step": 504
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.210714285714286e-05,
      "loss": 2.5676,
      "step": 505
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.2071428571428575e-05,
      "loss": 2.7445,
      "step": 506
    },
    {
      "epoch": 0.72,
      "learning_rate": 3.203571428571428e-05,
      "loss": 2.8537,
      "step": 507
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.2000000000000005e-05,
      "loss": 2.4633,
      "step": 508
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.1964285714285714e-05,
      "loss": 2.6765,
      "step": 509
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.192857142857143e-05,
      "loss": 2.8459,
      "step": 510
    },
    {
      "epoch": 0.73,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.561371088027954,
      "eval_runtime": 73.3168,
      "eval_samples_per_second": 3.178,
      "eval_steps_per_second": 1.596,
      "step": 510
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.1892857142857145e-05,
      "loss": 2.5084,
      "step": 511
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.185714285714286e-05,
      "loss": 2.89,
      "step": 512
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.1821428571428575e-05,
      "loss": 2.5615,
      "step": 513
    },
    {
      "epoch": 0.73,
      "learning_rate": 3.1785714285714284e-05,
      "loss": 2.6337,
      "step": 514
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.175e-05,
      "loss": 2.406,
      "step": 515
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.1714285714285715e-05,
      "loss": 2.6726,
      "step": 516
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.167857142857143e-05,
      "loss": 2.4526,
      "step": 517
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.1642857142857145e-05,
      "loss": 2.513,
      "step": 518
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.160714285714286e-05,
      "loss": 2.6643,
      "step": 519
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.1571428571428576e-05,
      "loss": 2.7539,
      "step": 520
    },
    {
      "epoch": 0.74,
      "eval_cer": 0.9617069285903902,
      "eval_loss": 2.5477752685546875,
      "eval_runtime": 72.0985,
      "eval_samples_per_second": 3.232,
      "eval_steps_per_second": 1.623,
      "step": 520
    },
    {
      "epoch": 0.74,
      "learning_rate": 3.1535714285714285e-05,
      "loss": 2.5534,
      "step": 521
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.15e-05,
      "loss": 2.6776,
      "step": 522
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.1464285714285715e-05,
      "loss": 2.7496,
      "step": 523
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.142857142857143e-05,
      "loss": 2.6506,
      "step": 524
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.1392857142857146e-05,
      "loss": 2.5093,
      "step": 525
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.1357142857142855e-05,
      "loss": 2.5628,
      "step": 526
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.132142857142858e-05,
      "loss": 3.1371,
      "step": 527
    },
    {
      "epoch": 0.75,
      "learning_rate": 3.1285714285714285e-05,
      "loss": 2.6159,
      "step": 528
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.125e-05,
      "loss": 2.6751,
      "step": 529
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.1214285714285716e-05,
      "loss": 2.5009,
      "step": 530
    },
    {
      "epoch": 0.76,
      "eval_cer": 0.975909211574197,
      "eval_loss": 2.54797101020813,
      "eval_runtime": 80.1614,
      "eval_samples_per_second": 2.907,
      "eval_steps_per_second": 1.46,
      "step": 530
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.117857142857143e-05,
      "loss": 2.5406,
      "step": 531
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.114285714285715e-05,
      "loss": 2.782,
      "step": 532
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.1107142857142855e-05,
      "loss": 3.0685,
      "step": 533
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.107142857142857e-05,
      "loss": 2.7879,
      "step": 534
    },
    {
      "epoch": 0.76,
      "learning_rate": 3.1035714285714286e-05,
      "loss": 2.6146,
      "step": 535
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.1e-05,
      "loss": 2.5429,
      "step": 536
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.096428571428572e-05,
      "loss": 2.5264,
      "step": 537
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.092857142857143e-05,
      "loss": 3.0088,
      "step": 538
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.089285714285715e-05,
      "loss": 2.5488,
      "step": 539
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.0857142857142856e-05,
      "loss": 2.5815,
      "step": 540
    },
    {
      "epoch": 0.77,
      "eval_cer": 0.9611760021237059,
      "eval_loss": 2.5408248901367188,
      "eval_runtime": 77.9104,
      "eval_samples_per_second": 2.991,
      "eval_steps_per_second": 1.502,
      "step": 540
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.082142857142857e-05,
      "loss": 3.2373,
      "step": 541
    },
    {
      "epoch": 0.77,
      "learning_rate": 3.078571428571429e-05,
      "loss": 2.5931,
      "step": 542
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.075e-05,
      "loss": 2.964,
      "step": 543
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.071428571428572e-05,
      "loss": 2.7101,
      "step": 544
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.0678571428571426e-05,
      "loss": 2.5255,
      "step": 545
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.064285714285715e-05,
      "loss": 2.5823,
      "step": 546
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.060714285714286e-05,
      "loss": 2.4255,
      "step": 547
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.057142857142857e-05,
      "loss": 2.665,
      "step": 548
    },
    {
      "epoch": 0.78,
      "learning_rate": 3.053571428571429e-05,
      "loss": 2.7819,
      "step": 549
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.05e-05,
      "loss": 2.6484,
      "step": 550
    },
    {
      "epoch": 0.79,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.508286952972412,
      "eval_runtime": 74.1828,
      "eval_samples_per_second": 3.141,
      "eval_steps_per_second": 1.577,
      "step": 550
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.0464285714285718e-05,
      "loss": 2.5077,
      "step": 551
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.042857142857143e-05,
      "loss": 2.6599,
      "step": 552
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.0392857142857145e-05,
      "loss": 2.8192,
      "step": 553
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.0357142857142857e-05,
      "loss": 2.7167,
      "step": 554
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.0321428571428573e-05,
      "loss": 2.4917,
      "step": 555
    },
    {
      "epoch": 0.79,
      "learning_rate": 3.0285714285714288e-05,
      "loss": 2.8507,
      "step": 556
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.025e-05,
      "loss": 2.6671,
      "step": 557
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.021428571428572e-05,
      "loss": 2.3206,
      "step": 558
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.0178571428571427e-05,
      "loss": 2.7347,
      "step": 559
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.0142857142857146e-05,
      "loss": 2.8842,
      "step": 560
    },
    {
      "epoch": 0.8,
      "eval_cer": 0.961441465357048,
      "eval_loss": 2.4957668781280518,
      "eval_runtime": 75.7619,
      "eval_samples_per_second": 3.075,
      "eval_steps_per_second": 1.544,
      "step": 560
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.0107142857142855e-05,
      "loss": 2.505,
      "step": 561
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.0071428571428573e-05,
      "loss": 2.6237,
      "step": 562
    },
    {
      "epoch": 0.8,
      "learning_rate": 3.003571428571429e-05,
      "loss": 2.6529,
      "step": 563
    },
    {
      "epoch": 0.81,
      "learning_rate": 3e-05,
      "loss": 2.6236,
      "step": 564
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.9964285714285716e-05,
      "loss": 2.6593,
      "step": 565
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.9928571428571428e-05,
      "loss": 2.8299,
      "step": 566
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.9892857142857143e-05,
      "loss": 2.6758,
      "step": 567
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.9857142857142862e-05,
      "loss": 2.6078,
      "step": 568
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.982142857142857e-05,
      "loss": 2.633,
      "step": 569
    },
    {
      "epoch": 0.81,
      "learning_rate": 2.978571428571429e-05,
      "loss": 2.7107,
      "step": 570
    },
    {
      "epoch": 0.81,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.496251344680786,
      "eval_runtime": 75.076,
      "eval_samples_per_second": 3.104,
      "eval_steps_per_second": 1.558,
      "step": 570
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.975e-05,
      "loss": 2.4856,
      "step": 571
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.9714285714285717e-05,
      "loss": 2.4351,
      "step": 572
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.967857142857143e-05,
      "loss": 2.3956,
      "step": 573
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.9642857142857144e-05,
      "loss": 2.4607,
      "step": 574
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.960714285714286e-05,
      "loss": 2.4501,
      "step": 575
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.957142857142857e-05,
      "loss": 2.5525,
      "step": 576
    },
    {
      "epoch": 0.82,
      "learning_rate": 2.953571428571429e-05,
      "loss": 2.3872,
      "step": 577
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.95e-05,
      "loss": 2.8644,
      "step": 578
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.9464285714285718e-05,
      "loss": 2.7064,
      "step": 579
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.9428571428571426e-05,
      "loss": 2.5344,
      "step": 580
    },
    {
      "epoch": 0.83,
      "eval_cer": 0.9743827979824794,
      "eval_loss": 2.511719226837158,
      "eval_runtime": 76.2255,
      "eval_samples_per_second": 3.057,
      "eval_steps_per_second": 1.535,
      "step": 580
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.9392857142857145e-05,
      "loss": 2.5604,
      "step": 581
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.935714285714286e-05,
      "loss": 2.8644,
      "step": 582
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.9321428571428572e-05,
      "loss": 2.6903,
      "step": 583
    },
    {
      "epoch": 0.83,
      "learning_rate": 2.9285714285714288e-05,
      "loss": 2.5982,
      "step": 584
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.925e-05,
      "loss": 2.6381,
      "step": 585
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.9214285714285715e-05,
      "loss": 2.4285,
      "step": 586
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.9178571428571427e-05,
      "loss": 2.9153,
      "step": 587
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.9142857142857146e-05,
      "loss": 2.5184,
      "step": 588
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.910714285714286e-05,
      "loss": 2.4554,
      "step": 589
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.9071428571428573e-05,
      "loss": 2.8028,
      "step": 590
    },
    {
      "epoch": 0.84,
      "eval_cer": 0.9757764799575259,
      "eval_loss": 2.484558343887329,
      "eval_runtime": 78.5339,
      "eval_samples_per_second": 2.967,
      "eval_steps_per_second": 1.49,
      "step": 590
    },
    {
      "epoch": 0.84,
      "learning_rate": 2.9035714285714288e-05,
      "loss": 2.5016,
      "step": 591
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.9e-05,
      "loss": 2.4666,
      "step": 592
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.8964285714285716e-05,
      "loss": 2.532,
      "step": 593
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.8928571428571434e-05,
      "loss": 2.511,
      "step": 594
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.8892857142857143e-05,
      "loss": 2.5018,
      "step": 595
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.885714285714286e-05,
      "loss": 2.4429,
      "step": 596
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.882142857142857e-05,
      "loss": 2.5323,
      "step": 597
    },
    {
      "epoch": 0.85,
      "learning_rate": 2.878571428571429e-05,
      "loss": 2.4513,
      "step": 598
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.8749999999999997e-05,
      "loss": 2.6701,
      "step": 599
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.8714285714285716e-05,
      "loss": 2.5353,
      "step": 600
    },
    {
      "epoch": 0.86,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.4851481914520264,
      "eval_runtime": 72.4661,
      "eval_samples_per_second": 3.215,
      "eval_steps_per_second": 1.615,
      "step": 600
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.867857142857143e-05,
      "loss": 2.6942,
      "step": 601
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.8642857142857144e-05,
      "loss": 2.6522,
      "step": 602
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.860714285714286e-05,
      "loss": 2.6789,
      "step": 603
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.857142857142857e-05,
      "loss": 2.5314,
      "step": 604
    },
    {
      "epoch": 0.86,
      "learning_rate": 2.8535714285714286e-05,
      "loss": 2.9271,
      "step": 605
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.8499999999999998e-05,
      "loss": 2.4708,
      "step": 606
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.8464285714285717e-05,
      "loss": 2.5456,
      "step": 607
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.8428571428571432e-05,
      "loss": 2.4632,
      "step": 608
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.8392857142857144e-05,
      "loss": 2.4282,
      "step": 609
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.835714285714286e-05,
      "loss": 2.4047,
      "step": 610
    },
    {
      "epoch": 0.87,
      "eval_cer": 0.9780329174409345,
      "eval_loss": 2.4922420978546143,
      "eval_runtime": 74.8004,
      "eval_samples_per_second": 3.115,
      "eval_steps_per_second": 1.564,
      "step": 610
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.832142857142857e-05,
      "loss": 2.7432,
      "step": 611
    },
    {
      "epoch": 0.87,
      "learning_rate": 2.8285714285714287e-05,
      "loss": 2.7395,
      "step": 612
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.825e-05,
      "loss": 2.4621,
      "step": 613
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.8214285714285714e-05,
      "loss": 2.4801,
      "step": 614
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.8178571428571433e-05,
      "loss": 2.4547,
      "step": 615
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.814285714285714e-05,
      "loss": 2.3703,
      "step": 616
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.810714285714286e-05,
      "loss": 2.5179,
      "step": 617
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.8071428571428572e-05,
      "loss": 2.45,
      "step": 618
    },
    {
      "epoch": 0.88,
      "learning_rate": 2.8035714285714288e-05,
      "loss": 2.7504,
      "step": 619
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.8000000000000003e-05,
      "loss": 2.7013,
      "step": 620
    },
    {
      "epoch": 0.89,
      "eval_cer": 0.9770374303159013,
      "eval_loss": 2.4898478984832764,
      "eval_runtime": 79.184,
      "eval_samples_per_second": 2.943,
      "eval_steps_per_second": 1.478,
      "step": 620
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.7964285714285715e-05,
      "loss": 2.5037,
      "step": 621
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.792857142857143e-05,
      "loss": 2.4585,
      "step": 622
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.7892857142857142e-05,
      "loss": 2.7427,
      "step": 623
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.785714285714286e-05,
      "loss": 2.7849,
      "step": 624
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.782142857142857e-05,
      "loss": 2.5837,
      "step": 625
    },
    {
      "epoch": 0.89,
      "learning_rate": 2.778571428571429e-05,
      "loss": 2.6257,
      "step": 626
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.7750000000000004e-05,
      "loss": 2.6948,
      "step": 627
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.7714285714285716e-05,
      "loss": 2.4841,
      "step": 628
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.767857142857143e-05,
      "loss": 2.482,
      "step": 629
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.7642857142857143e-05,
      "loss": 2.459,
      "step": 630
    },
    {
      "epoch": 0.9,
      "eval_cer": 0.9775019909742501,
      "eval_loss": 2.473936080932617,
      "eval_runtime": 74.3858,
      "eval_samples_per_second": 3.132,
      "eval_steps_per_second": 1.573,
      "step": 630
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.760714285714286e-05,
      "loss": 2.1141,
      "step": 631
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.757142857142857e-05,
      "loss": 2.4295,
      "step": 632
    },
    {
      "epoch": 0.9,
      "learning_rate": 2.7535714285714286e-05,
      "loss": 2.5661,
      "step": 633
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.7500000000000004e-05,
      "loss": 2.475,
      "step": 634
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.7464285714285713e-05,
      "loss": 2.5536,
      "step": 635
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.742857142857143e-05,
      "loss": 2.445,
      "step": 636
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.7392857142857144e-05,
      "loss": 2.4078,
      "step": 637
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.735714285714286e-05,
      "loss": 2.6499,
      "step": 638
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.732142857142857e-05,
      "loss": 2.3519,
      "step": 639
    },
    {
      "epoch": 0.91,
      "learning_rate": 2.7285714285714286e-05,
      "loss": 2.2828,
      "step": 640
    },
    {
      "epoch": 0.91,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.4764413833618164,
      "eval_runtime": 76.3527,
      "eval_samples_per_second": 3.052,
      "eval_steps_per_second": 1.532,
      "step": 640
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.725e-05,
      "loss": 2.4647,
      "step": 641
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.7214285714285714e-05,
      "loss": 2.6792,
      "step": 642
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.7178571428571432e-05,
      "loss": 2.3772,
      "step": 643
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.714285714285714e-05,
      "loss": 2.5133,
      "step": 644
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.710714285714286e-05,
      "loss": 2.459,
      "step": 645
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.7071428571428575e-05,
      "loss": 2.4174,
      "step": 646
    },
    {
      "epoch": 0.92,
      "learning_rate": 2.7035714285714287e-05,
      "loss": 2.6248,
      "step": 647
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.7000000000000002e-05,
      "loss": 2.4897,
      "step": 648
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.6964285714285714e-05,
      "loss": 2.4478,
      "step": 649
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.692857142857143e-05,
      "loss": 2.4081,
      "step": 650
    },
    {
      "epoch": 0.93,
      "eval_cer": 0.9611096363153703,
      "eval_loss": 2.4617395401000977,
      "eval_runtime": 77.0618,
      "eval_samples_per_second": 3.024,
      "eval_steps_per_second": 1.518,
      "step": 650
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.689285714285714e-05,
      "loss": 2.5667,
      "step": 651
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.6857142857142857e-05,
      "loss": 3.0602,
      "step": 652
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.6821428571428576e-05,
      "loss": 2.613,
      "step": 653
    },
    {
      "epoch": 0.93,
      "learning_rate": 2.6785714285714288e-05,
      "loss": 2.6663,
      "step": 654
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6750000000000003e-05,
      "loss": 2.4027,
      "step": 655
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6714285714285715e-05,
      "loss": 2.5566,
      "step": 656
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.667857142857143e-05,
      "loss": 2.44,
      "step": 657
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6642857142857142e-05,
      "loss": 2.6236,
      "step": 658
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6607142857142858e-05,
      "loss": 2.3887,
      "step": 659
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6571428571428576e-05,
      "loss": 2.451,
      "step": 660
    },
    {
      "epoch": 0.94,
      "eval_cer": 0.9740509689408017,
      "eval_loss": 2.431640625,
      "eval_runtime": 74.2085,
      "eval_samples_per_second": 3.14,
      "eval_steps_per_second": 1.577,
      "step": 660
    },
    {
      "epoch": 0.94,
      "learning_rate": 2.6535714285714285e-05,
      "loss": 2.615,
      "step": 661
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.6500000000000004e-05,
      "loss": 2.3016,
      "step": 662
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.6464285714285712e-05,
      "loss": 2.5249,
      "step": 663
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.642857142857143e-05,
      "loss": 2.6232,
      "step": 664
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.6392857142857143e-05,
      "loss": 2.4943,
      "step": 665
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.635714285714286e-05,
      "loss": 2.3993,
      "step": 666
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.6321428571428574e-05,
      "loss": 2.5705,
      "step": 667
    },
    {
      "epoch": 0.95,
      "learning_rate": 2.6285714285714286e-05,
      "loss": 2.7006,
      "step": 668
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.625e-05,
      "loss": 2.5145,
      "step": 669
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.6214285714285713e-05,
      "loss": 2.5599,
      "step": 670
    },
    {
      "epoch": 0.96,
      "eval_cer": 0.9723254579240775,
      "eval_loss": 2.440812110900879,
      "eval_runtime": 71.7017,
      "eval_samples_per_second": 3.25,
      "eval_steps_per_second": 1.632,
      "step": 670
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.617857142857143e-05,
      "loss": 2.5992,
      "step": 671
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.6142857142857147e-05,
      "loss": 3.0045,
      "step": 672
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.610714285714286e-05,
      "loss": 2.3911,
      "step": 673
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.6071428571428574e-05,
      "loss": 2.946,
      "step": 674
    },
    {
      "epoch": 0.96,
      "learning_rate": 2.6035714285714286e-05,
      "loss": 2.4556,
      "step": 675
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.6000000000000002e-05,
      "loss": 2.474,
      "step": 676
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.5964285714285714e-05,
      "loss": 2.5949,
      "step": 677
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.592857142857143e-05,
      "loss": 2.8015,
      "step": 678
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.5892857142857148e-05,
      "loss": 2.6686,
      "step": 679
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.5857142857142856e-05,
      "loss": 2.8161,
      "step": 680
    },
    {
      "epoch": 0.97,
      "eval_cer": 0.9637642686487922,
      "eval_loss": 2.456733226776123,
      "eval_runtime": 76.5004,
      "eval_samples_per_second": 3.046,
      "eval_steps_per_second": 1.529,
      "step": 680
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.5821428571428575e-05,
      "loss": 2.5977,
      "step": 681
    },
    {
      "epoch": 0.97,
      "learning_rate": 2.5785714285714284e-05,
      "loss": 2.5251,
      "step": 682
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5750000000000002e-05,
      "loss": 2.4171,
      "step": 683
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5714285714285714e-05,
      "loss": 2.4032,
      "step": 684
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.567857142857143e-05,
      "loss": 2.5712,
      "step": 685
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5642857142857145e-05,
      "loss": 2.4334,
      "step": 686
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5607142857142857e-05,
      "loss": 2.6077,
      "step": 687
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5571428571428572e-05,
      "loss": 2.5282,
      "step": 688
    },
    {
      "epoch": 0.98,
      "learning_rate": 2.5535714285714284e-05,
      "loss": 2.3641,
      "step": 689
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5500000000000003e-05,
      "loss": 2.5251,
      "step": 690
    },
    {
      "epoch": 0.99,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.4401378631591797,
      "eval_runtime": 70.889,
      "eval_samples_per_second": 3.287,
      "eval_steps_per_second": 1.65,
      "step": 690
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5464285714285712e-05,
      "loss": 2.4605,
      "step": 691
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.542857142857143e-05,
      "loss": 2.1895,
      "step": 692
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5392857142857146e-05,
      "loss": 2.7313,
      "step": 693
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5357142857142858e-05,
      "loss": 2.409,
      "step": 694
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5321428571428573e-05,
      "loss": 2.3507,
      "step": 695
    },
    {
      "epoch": 0.99,
      "learning_rate": 2.5285714285714285e-05,
      "loss": 2.5341,
      "step": 696
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.525e-05,
      "loss": 2.3956,
      "step": 697
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.521428571428572e-05,
      "loss": 2.6438,
      "step": 698
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.5178571428571428e-05,
      "loss": 2.4066,
      "step": 699
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.5142857142857147e-05,
      "loss": 2.791,
      "step": 700
    },
    {
      "epoch": 1.0,
      "eval_cer": 0.9737855057074595,
      "eval_loss": 2.425037384033203,
      "eval_runtime": 77.1947,
      "eval_samples_per_second": 3.018,
      "eval_steps_per_second": 1.516,
      "step": 700
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.510714285714286e-05,
      "loss": 2.3511,
      "step": 701
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.5071428571428574e-05,
      "loss": 2.5991,
      "step": 702
    },
    {
      "epoch": 1.0,
      "learning_rate": 2.5035714285714286e-05,
      "loss": 2.5289,
      "step": 703
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.5e-05,
      "loss": 2.3273,
      "step": 704
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.4964285714285717e-05,
      "loss": 2.6067,
      "step": 705
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.492857142857143e-05,
      "loss": 2.5956,
      "step": 706
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.4892857142857144e-05,
      "loss": 2.6098,
      "step": 707
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.485714285714286e-05,
      "loss": 2.1864,
      "step": 708
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.4821428571428575e-05,
      "loss": 2.5877,
      "step": 709
    },
    {
      "epoch": 1.01,
      "learning_rate": 2.4785714285714287e-05,
      "loss": 2.7681,
      "step": 710
    },
    {
      "epoch": 1.01,
      "eval_cer": 0.9688080700822936,
      "eval_loss": 2.406101703643799,
      "eval_runtime": 73.5652,
      "eval_samples_per_second": 3.167,
      "eval_steps_per_second": 1.59,
      "step": 710
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.4750000000000002e-05,
      "loss": 2.4451,
      "step": 711
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.4714285714285714e-05,
      "loss": 2.379,
      "step": 712
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.467857142857143e-05,
      "loss": 2.4172,
      "step": 713
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.4642857142857145e-05,
      "loss": 2.4222,
      "step": 714
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.460714285714286e-05,
      "loss": 2.5958,
      "step": 715
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.4571428571428572e-05,
      "loss": 2.6688,
      "step": 716
    },
    {
      "epoch": 1.02,
      "learning_rate": 2.4535714285714287e-05,
      "loss": 2.2448,
      "step": 717
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.45e-05,
      "loss": 2.2827,
      "step": 718
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.4464285714285715e-05,
      "loss": 2.9178,
      "step": 719
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.442857142857143e-05,
      "loss": 2.4466,
      "step": 720
    },
    {
      "epoch": 1.03,
      "eval_cer": 0.9753782851075126,
      "eval_loss": 2.4072868824005127,
      "eval_runtime": 71.2514,
      "eval_samples_per_second": 3.27,
      "eval_steps_per_second": 1.642,
      "step": 720
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.4392857142857145e-05,
      "loss": 2.3715,
      "step": 721
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.4357142857142857e-05,
      "loss": 2.4151,
      "step": 722
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.4321428571428573e-05,
      "loss": 2.3594,
      "step": 723
    },
    {
      "epoch": 1.03,
      "learning_rate": 2.4285714285714288e-05,
      "loss": 2.4716,
      "step": 724
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.425e-05,
      "loss": 2.3707,
      "step": 725
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.4214285714285715e-05,
      "loss": 2.4156,
      "step": 726
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.417857142857143e-05,
      "loss": 2.4189,
      "step": 727
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.4142857142857146e-05,
      "loss": 2.4581,
      "step": 728
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.4107142857142858e-05,
      "loss": 2.753,
      "step": 729
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.4071428571428573e-05,
      "loss": 2.3322,
      "step": 730
    },
    {
      "epoch": 1.04,
      "eval_cer": 0.9767719670825591,
      "eval_loss": 2.414685010910034,
      "eval_runtime": 75.8588,
      "eval_samples_per_second": 3.071,
      "eval_steps_per_second": 1.542,
      "step": 730
    },
    {
      "epoch": 1.04,
      "learning_rate": 2.4035714285714285e-05,
      "loss": 2.4952,
      "step": 731
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.4e-05,
      "loss": 2.3477,
      "step": 732
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.3964285714285713e-05,
      "loss": 2.5903,
      "step": 733
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.392857142857143e-05,
      "loss": 2.3468,
      "step": 734
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.3892857142857143e-05,
      "loss": 2.4398,
      "step": 735
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.385714285714286e-05,
      "loss": 2.586,
      "step": 736
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.3821428571428574e-05,
      "loss": 2.6776,
      "step": 737
    },
    {
      "epoch": 1.05,
      "learning_rate": 2.3785714285714286e-05,
      "loss": 2.6721,
      "step": 738
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.375e-05,
      "loss": 2.4757,
      "step": 739
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.3714285714285717e-05,
      "loss": 2.6704,
      "step": 740
    },
    {
      "epoch": 1.06,
      "eval_cer": 0.9570613220069021,
      "eval_loss": 2.4364845752716064,
      "eval_runtime": 75.2688,
      "eval_samples_per_second": 3.096,
      "eval_steps_per_second": 1.554,
      "step": 740
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.3678571428571432e-05,
      "loss": 2.3447,
      "step": 741
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.3642857142857144e-05,
      "loss": 2.4893,
      "step": 742
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.360714285714286e-05,
      "loss": 2.5197,
      "step": 743
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.357142857142857e-05,
      "loss": 2.6463,
      "step": 744
    },
    {
      "epoch": 1.06,
      "learning_rate": 2.3535714285714287e-05,
      "loss": 2.3813,
      "step": 745
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.35e-05,
      "loss": 2.3388,
      "step": 746
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.3464285714285717e-05,
      "loss": 2.4391,
      "step": 747
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.342857142857143e-05,
      "loss": 2.7473,
      "step": 748
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.3392857142857145e-05,
      "loss": 2.3234,
      "step": 749
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.3357142857142857e-05,
      "loss": 2.3501,
      "step": 750
    },
    {
      "epoch": 1.07,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.410749912261963,
      "eval_runtime": 65.8006,
      "eval_samples_per_second": 3.541,
      "eval_steps_per_second": 1.778,
      "step": 750
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.3321428571428572e-05,
      "loss": 2.4501,
      "step": 751
    },
    {
      "epoch": 1.07,
      "learning_rate": 2.3285714285714287e-05,
      "loss": 2.6235,
      "step": 752
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3250000000000003e-05,
      "loss": 2.6306,
      "step": 753
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3214285714285715e-05,
      "loss": 2.6785,
      "step": 754
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.317857142857143e-05,
      "loss": 2.4314,
      "step": 755
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3142857142857145e-05,
      "loss": 2.3911,
      "step": 756
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3107142857142857e-05,
      "loss": 2.687,
      "step": 757
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3071428571428573e-05,
      "loss": 2.365,
      "step": 758
    },
    {
      "epoch": 1.08,
      "learning_rate": 2.3035714285714285e-05,
      "loss": 2.3013,
      "step": 759
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.3000000000000003e-05,
      "loss": 2.6101,
      "step": 760
    },
    {
      "epoch": 1.09,
      "eval_cer": 0.9574595168569153,
      "eval_loss": 2.4018094539642334,
      "eval_runtime": 72.1692,
      "eval_samples_per_second": 3.229,
      "eval_steps_per_second": 1.621,
      "step": 760
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.2964285714285715e-05,
      "loss": 2.5978,
      "step": 761
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.292857142857143e-05,
      "loss": 2.3067,
      "step": 762
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.2892857142857143e-05,
      "loss": 2.6956,
      "step": 763
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.2857142857142858e-05,
      "loss": 2.4171,
      "step": 764
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.282142857142857e-05,
      "loss": 2.3,
      "step": 765
    },
    {
      "epoch": 1.09,
      "learning_rate": 2.278571428571429e-05,
      "loss": 2.7669,
      "step": 766
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.275e-05,
      "loss": 2.9065,
      "step": 767
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.2714285714285716e-05,
      "loss": 2.3893,
      "step": 768
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.2678571428571428e-05,
      "loss": 2.1859,
      "step": 769
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.2642857142857143e-05,
      "loss": 2.3502,
      "step": 770
    },
    {
      "epoch": 1.1,
      "eval_cer": 0.9739846031324662,
      "eval_loss": 2.4191720485687256,
      "eval_runtime": 74.2017,
      "eval_samples_per_second": 3.14,
      "eval_steps_per_second": 1.577,
      "step": 770
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.260714285714286e-05,
      "loss": 2.4649,
      "step": 771
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.257142857142857e-05,
      "loss": 2.3908,
      "step": 772
    },
    {
      "epoch": 1.1,
      "learning_rate": 2.253571428571429e-05,
      "loss": 2.2373,
      "step": 773
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.25e-05,
      "loss": 2.4337,
      "step": 774
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.2464285714285717e-05,
      "loss": 2.6153,
      "step": 775
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.242857142857143e-05,
      "loss": 2.2347,
      "step": 776
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.2392857142857144e-05,
      "loss": 2.4555,
      "step": 777
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.2357142857142856e-05,
      "loss": 2.516,
      "step": 778
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.2321428571428575e-05,
      "loss": 2.2351,
      "step": 779
    },
    {
      "epoch": 1.11,
      "learning_rate": 2.2285714285714287e-05,
      "loss": 2.4479,
      "step": 780
    },
    {
      "epoch": 1.11,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3944127559661865,
      "eval_runtime": 70.1313,
      "eval_samples_per_second": 3.322,
      "eval_steps_per_second": 1.668,
      "step": 780
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.2250000000000002e-05,
      "loss": 2.455,
      "step": 781
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.2214285714285714e-05,
      "loss": 2.3744,
      "step": 782
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.217857142857143e-05,
      "loss": 2.4942,
      "step": 783
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.214285714285714e-05,
      "loss": 2.438,
      "step": 784
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.2107142857142857e-05,
      "loss": 2.2942,
      "step": 785
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.2071428571428572e-05,
      "loss": 2.4609,
      "step": 786
    },
    {
      "epoch": 1.12,
      "learning_rate": 2.2035714285714287e-05,
      "loss": 2.4251,
      "step": 787
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.2000000000000003e-05,
      "loss": 2.273,
      "step": 788
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.1964285714285715e-05,
      "loss": 2.6086,
      "step": 789
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.192857142857143e-05,
      "loss": 2.4864,
      "step": 790
    },
    {
      "epoch": 1.13,
      "eval_cer": 0.9610432705070348,
      "eval_loss": 2.4093406200408936,
      "eval_runtime": 72.6828,
      "eval_samples_per_second": 3.206,
      "eval_steps_per_second": 1.61,
      "step": 790
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.1892857142857142e-05,
      "loss": 2.6,
      "step": 791
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.185714285714286e-05,
      "loss": 2.3233,
      "step": 792
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.1821428571428573e-05,
      "loss": 2.4164,
      "step": 793
    },
    {
      "epoch": 1.13,
      "learning_rate": 2.1785714285714288e-05,
      "loss": 2.5613,
      "step": 794
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.175e-05,
      "loss": 2.3779,
      "step": 795
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1714285714285715e-05,
      "loss": 2.6096,
      "step": 796
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1678571428571427e-05,
      "loss": 2.252,
      "step": 797
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1642857142857146e-05,
      "loss": 2.3711,
      "step": 798
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1607142857142858e-05,
      "loss": 2.3337,
      "step": 799
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1571428571428574e-05,
      "loss": 2.7827,
      "step": 800
    },
    {
      "epoch": 1.14,
      "eval_cer": 0.9739846031324662,
      "eval_loss": 2.3948779106140137,
      "eval_runtime": 74.3916,
      "eval_samples_per_second": 3.132,
      "eval_steps_per_second": 1.573,
      "step": 800
    },
    {
      "epoch": 1.14,
      "learning_rate": 2.1535714285714285e-05,
      "loss": 2.3712,
      "step": 801
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.15e-05,
      "loss": 2.583,
      "step": 802
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.1464285714285716e-05,
      "loss": 2.4502,
      "step": 803
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.1428571428571428e-05,
      "loss": 2.4405,
      "step": 804
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.1392857142857143e-05,
      "loss": 2.3525,
      "step": 805
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.135714285714286e-05,
      "loss": 2.371,
      "step": 806
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.1321428571428574e-05,
      "loss": 2.417,
      "step": 807
    },
    {
      "epoch": 1.15,
      "learning_rate": 2.1285714285714286e-05,
      "loss": 2.4333,
      "step": 808
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.125e-05,
      "loss": 2.3429,
      "step": 809
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.1214285714285713e-05,
      "loss": 2.491,
      "step": 810
    },
    {
      "epoch": 1.16,
      "eval_cer": 0.9742500663658084,
      "eval_loss": 2.3672420978546143,
      "eval_runtime": 72.8348,
      "eval_samples_per_second": 3.199,
      "eval_steps_per_second": 1.606,
      "step": 810
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.1178571428571432e-05,
      "loss": 2.4522,
      "step": 811
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.1142857142857144e-05,
      "loss": 2.3757,
      "step": 812
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.110714285714286e-05,
      "loss": 2.4603,
      "step": 813
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.107142857142857e-05,
      "loss": 2.3228,
      "step": 814
    },
    {
      "epoch": 1.16,
      "learning_rate": 2.1035714285714287e-05,
      "loss": 2.5547,
      "step": 815
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.1e-05,
      "loss": 2.3474,
      "step": 816
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.0964285714285714e-05,
      "loss": 2.4927,
      "step": 817
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.092857142857143e-05,
      "loss": 2.7481,
      "step": 818
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.0892857142857145e-05,
      "loss": 2.3617,
      "step": 819
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.0857142857142857e-05,
      "loss": 2.4346,
      "step": 820
    },
    {
      "epoch": 1.17,
      "eval_cer": 0.9609105388903637,
      "eval_loss": 2.409487247467041,
      "eval_runtime": 74.3423,
      "eval_samples_per_second": 3.134,
      "eval_steps_per_second": 1.574,
      "step": 820
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.0821428571428572e-05,
      "loss": 2.5359,
      "step": 821
    },
    {
      "epoch": 1.17,
      "learning_rate": 2.0785714285714288e-05,
      "loss": 2.4148,
      "step": 822
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.075e-05,
      "loss": 2.3253,
      "step": 823
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.0714285714285718e-05,
      "loss": 2.5388,
      "step": 824
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.067857142857143e-05,
      "loss": 2.365,
      "step": 825
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.0642857142857146e-05,
      "loss": 2.5885,
      "step": 826
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.0607142857142858e-05,
      "loss": 2.2593,
      "step": 827
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.0571428571428573e-05,
      "loss": 2.8819,
      "step": 828
    },
    {
      "epoch": 1.18,
      "learning_rate": 2.0535714285714285e-05,
      "loss": 2.3054,
      "step": 829
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.05e-05,
      "loss": 2.3355,
      "step": 830
    },
    {
      "epoch": 1.19,
      "eval_cer": 0.9609769046986992,
      "eval_loss": 2.3964879512786865,
      "eval_runtime": 73.2402,
      "eval_samples_per_second": 3.181,
      "eval_steps_per_second": 1.597,
      "step": 830
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.0464285714285716e-05,
      "loss": 2.1563,
      "step": 831
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.042857142857143e-05,
      "loss": 2.5963,
      "step": 832
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.0392857142857143e-05,
      "loss": 2.3938,
      "step": 833
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.0357142857142858e-05,
      "loss": 2.3165,
      "step": 834
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.032142857142857e-05,
      "loss": 2.5788,
      "step": 835
    },
    {
      "epoch": 1.19,
      "learning_rate": 2.0285714285714286e-05,
      "loss": 2.1861,
      "step": 836
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.025e-05,
      "loss": 2.4219,
      "step": 837
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.0214285714285716e-05,
      "loss": 2.4462,
      "step": 838
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.017857142857143e-05,
      "loss": 2.4253,
      "step": 839
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.0142857142857144e-05,
      "loss": 2.4464,
      "step": 840
    },
    {
      "epoch": 1.2,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3676204681396484,
      "eval_runtime": 71.9127,
      "eval_samples_per_second": 3.24,
      "eval_steps_per_second": 1.627,
      "step": 840
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.010714285714286e-05,
      "loss": 2.3345,
      "step": 841
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.007142857142857e-05,
      "loss": 2.4251,
      "step": 842
    },
    {
      "epoch": 1.2,
      "learning_rate": 2.0035714285714286e-05,
      "loss": 2.4349,
      "step": 843
    },
    {
      "epoch": 1.21,
      "learning_rate": 2e-05,
      "loss": 2.5821,
      "step": 844
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.9964285714285717e-05,
      "loss": 2.4223,
      "step": 845
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.992857142857143e-05,
      "loss": 2.5976,
      "step": 846
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.9892857142857144e-05,
      "loss": 2.3877,
      "step": 847
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.9857142857142856e-05,
      "loss": 2.4851,
      "step": 848
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.982142857142857e-05,
      "loss": 2.4592,
      "step": 849
    },
    {
      "epoch": 1.21,
      "learning_rate": 1.9785714285714287e-05,
      "loss": 2.2612,
      "step": 850
    },
    {
      "epoch": 1.21,
      "eval_cer": 0.9704008494823467,
      "eval_loss": 2.3766424655914307,
      "eval_runtime": 73.5383,
      "eval_samples_per_second": 3.168,
      "eval_steps_per_second": 1.591,
      "step": 850
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9750000000000002e-05,
      "loss": 2.7221,
      "step": 851
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9714285714285714e-05,
      "loss": 2.4378,
      "step": 852
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.967857142857143e-05,
      "loss": 2.4311,
      "step": 853
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9642857142857145e-05,
      "loss": 2.1722,
      "step": 854
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9607142857142857e-05,
      "loss": 2.1477,
      "step": 855
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9571428571428572e-05,
      "loss": 2.4805,
      "step": 856
    },
    {
      "epoch": 1.22,
      "learning_rate": 1.9535714285714288e-05,
      "loss": 2.475,
      "step": 857
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.9500000000000003e-05,
      "loss": 2.3965,
      "step": 858
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.9464285714285715e-05,
      "loss": 2.486,
      "step": 859
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.942857142857143e-05,
      "loss": 2.5338,
      "step": 860
    },
    {
      "epoch": 1.23,
      "eval_cer": 0.9597159543403239,
      "eval_loss": 2.383744478225708,
      "eval_runtime": 74.7495,
      "eval_samples_per_second": 3.117,
      "eval_steps_per_second": 1.565,
      "step": 860
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.9392857142857142e-05,
      "loss": 2.4133,
      "step": 861
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.9357142857142858e-05,
      "loss": 2.4305,
      "step": 862
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.9321428571428573e-05,
      "loss": 2.3513,
      "step": 863
    },
    {
      "epoch": 1.23,
      "learning_rate": 1.928571428571429e-05,
      "loss": 2.4114,
      "step": 864
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.925e-05,
      "loss": 2.9338,
      "step": 865
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.9214285714285716e-05,
      "loss": 2.7388,
      "step": 866
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.9178571428571428e-05,
      "loss": 2.5219,
      "step": 867
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.9142857142857143e-05,
      "loss": 2.46,
      "step": 868
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.910714285714286e-05,
      "loss": 2.2643,
      "step": 869
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.9071428571428574e-05,
      "loss": 2.4535,
      "step": 870
    },
    {
      "epoch": 1.24,
      "eval_cer": 0.967878948765596,
      "eval_loss": 2.3535943031311035,
      "eval_runtime": 73.0611,
      "eval_samples_per_second": 3.189,
      "eval_steps_per_second": 1.601,
      "step": 870
    },
    {
      "epoch": 1.24,
      "learning_rate": 1.9035714285714286e-05,
      "loss": 2.6856,
      "step": 871
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.9e-05,
      "loss": 2.9028,
      "step": 872
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.8964285714285716e-05,
      "loss": 2.3363,
      "step": 873
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.892857142857143e-05,
      "loss": 2.4001,
      "step": 874
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.8892857142857144e-05,
      "loss": 2.9529,
      "step": 875
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.885714285714286e-05,
      "loss": 2.377,
      "step": 876
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.8821428571428574e-05,
      "loss": 2.4119,
      "step": 877
    },
    {
      "epoch": 1.25,
      "learning_rate": 1.8785714285714286e-05,
      "loss": 2.1767,
      "step": 878
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.8750000000000002e-05,
      "loss": 2.3401,
      "step": 879
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.8714285714285714e-05,
      "loss": 2.3101,
      "step": 880
    },
    {
      "epoch": 1.26,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3583714962005615,
      "eval_runtime": 74.9721,
      "eval_samples_per_second": 3.108,
      "eval_steps_per_second": 1.561,
      "step": 880
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.867857142857143e-05,
      "loss": 2.4309,
      "step": 881
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.864285714285714e-05,
      "loss": 2.367,
      "step": 882
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.860714285714286e-05,
      "loss": 2.5413,
      "step": 883
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.8571428571428572e-05,
      "loss": 2.4376,
      "step": 884
    },
    {
      "epoch": 1.26,
      "learning_rate": 1.8535714285714287e-05,
      "loss": 2.4695,
      "step": 885
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.85e-05,
      "loss": 2.2499,
      "step": 886
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.8464285714285714e-05,
      "loss": 2.5331,
      "step": 887
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.842857142857143e-05,
      "loss": 2.3832,
      "step": 888
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.8392857142857145e-05,
      "loss": 2.5626,
      "step": 889
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.835714285714286e-05,
      "loss": 2.4045,
      "step": 890
    },
    {
      "epoch": 1.27,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3508388996124268,
      "eval_runtime": 75.5944,
      "eval_samples_per_second": 3.082,
      "eval_steps_per_second": 1.548,
      "step": 890
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.8321428571428572e-05,
      "loss": 2.5674,
      "step": 891
    },
    {
      "epoch": 1.27,
      "learning_rate": 1.8285714285714288e-05,
      "loss": 2.3338,
      "step": 892
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.825e-05,
      "loss": 2.6233,
      "step": 893
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8214285714285715e-05,
      "loss": 2.242,
      "step": 894
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8178571428571427e-05,
      "loss": 2.3356,
      "step": 895
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8142857142857146e-05,
      "loss": 2.4296,
      "step": 896
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8107142857142858e-05,
      "loss": 2.3134,
      "step": 897
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8071428571428573e-05,
      "loss": 2.6397,
      "step": 898
    },
    {
      "epoch": 1.28,
      "learning_rate": 1.8035714285714285e-05,
      "loss": 2.3903,
      "step": 899
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.8e-05,
      "loss": 2.2121,
      "step": 900
    },
    {
      "epoch": 1.29,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.354097604751587,
      "eval_runtime": 74.4103,
      "eval_samples_per_second": 3.131,
      "eval_steps_per_second": 1.572,
      "step": 900
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.7964285714285712e-05,
      "loss": 2.2174,
      "step": 901
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.792857142857143e-05,
      "loss": 2.6706,
      "step": 902
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.7892857142857143e-05,
      "loss": 2.4925,
      "step": 903
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.785714285714286e-05,
      "loss": 2.574,
      "step": 904
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.7821428571428574e-05,
      "loss": 2.4683,
      "step": 905
    },
    {
      "epoch": 1.29,
      "learning_rate": 1.7785714285714286e-05,
      "loss": 2.5112,
      "step": 906
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.775e-05,
      "loss": 2.4117,
      "step": 907
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.7714285714285713e-05,
      "loss": 2.079,
      "step": 908
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.7678571428571432e-05,
      "loss": 2.3749,
      "step": 909
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.7642857142857144e-05,
      "loss": 2.2123,
      "step": 910
    },
    {
      "epoch": 1.3,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.357185125350952,
      "eval_runtime": 72.0185,
      "eval_samples_per_second": 3.235,
      "eval_steps_per_second": 1.625,
      "step": 910
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.760714285714286e-05,
      "loss": 2.5947,
      "step": 911
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.757142857142857e-05,
      "loss": 2.5813,
      "step": 912
    },
    {
      "epoch": 1.3,
      "learning_rate": 1.7535714285714287e-05,
      "loss": 2.2208,
      "step": 913
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.75e-05,
      "loss": 2.4576,
      "step": 914
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.7464285714285717e-05,
      "loss": 2.2353,
      "step": 915
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.742857142857143e-05,
      "loss": 2.4039,
      "step": 916
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.7392857142857145e-05,
      "loss": 2.2329,
      "step": 917
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.7357142857142856e-05,
      "loss": 2.3473,
      "step": 918
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.7321428571428572e-05,
      "loss": 2.3932,
      "step": 919
    },
    {
      "epoch": 1.31,
      "learning_rate": 1.7285714285714287e-05,
      "loss": 2.1142,
      "step": 920
    },
    {
      "epoch": 1.31,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.360193967819214,
      "eval_runtime": 72.5635,
      "eval_samples_per_second": 3.211,
      "eval_steps_per_second": 1.612,
      "step": 920
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.725e-05,
      "loss": 2.4258,
      "step": 921
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.7214285714285715e-05,
      "loss": 2.6141,
      "step": 922
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.717857142857143e-05,
      "loss": 2.2416,
      "step": 923
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.7142857142857145e-05,
      "loss": 2.3273,
      "step": 924
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.7107142857142857e-05,
      "loss": 2.4106,
      "step": 925
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.7071428571428573e-05,
      "loss": 2.43,
      "step": 926
    },
    {
      "epoch": 1.32,
      "learning_rate": 1.7035714285714285e-05,
      "loss": 2.4518,
      "step": 927
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.7000000000000003e-05,
      "loss": 2.5446,
      "step": 928
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.6964285714285715e-05,
      "loss": 1.981,
      "step": 929
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.692857142857143e-05,
      "loss": 2.185,
      "step": 930
    },
    {
      "epoch": 1.33,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3609461784362793,
      "eval_runtime": 74.9136,
      "eval_samples_per_second": 3.11,
      "eval_steps_per_second": 1.562,
      "step": 930
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.6892857142857143e-05,
      "loss": 2.5589,
      "step": 931
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.6857142857142858e-05,
      "loss": 2.3812,
      "step": 932
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.682142857142857e-05,
      "loss": 2.2992,
      "step": 933
    },
    {
      "epoch": 1.33,
      "learning_rate": 1.6785714285714285e-05,
      "loss": 2.192,
      "step": 934
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.675e-05,
      "loss": 2.4167,
      "step": 935
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.6714285714285716e-05,
      "loss": 2.3762,
      "step": 936
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.6678571428571428e-05,
      "loss": 2.2206,
      "step": 937
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.6642857142857143e-05,
      "loss": 2.3521,
      "step": 938
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.660714285714286e-05,
      "loss": 2.0605,
      "step": 939
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.657142857142857e-05,
      "loss": 2.3517,
      "step": 940
    },
    {
      "epoch": 1.34,
      "eval_cer": 0.972259092115742,
      "eval_loss": 2.349470615386963,
      "eval_runtime": 76.6255,
      "eval_samples_per_second": 3.041,
      "eval_steps_per_second": 1.527,
      "step": 940
    },
    {
      "epoch": 1.34,
      "learning_rate": 1.653571428571429e-05,
      "loss": 2.3751,
      "step": 941
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.65e-05,
      "loss": 2.3003,
      "step": 942
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.6464285714285717e-05,
      "loss": 2.3273,
      "step": 943
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.642857142857143e-05,
      "loss": 2.4344,
      "step": 944
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.6392857142857144e-05,
      "loss": 2.5492,
      "step": 945
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.6357142857142856e-05,
      "loss": 2.2523,
      "step": 946
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.632142857142857e-05,
      "loss": 2.3605,
      "step": 947
    },
    {
      "epoch": 1.35,
      "learning_rate": 1.6285714285714287e-05,
      "loss": 2.3746,
      "step": 948
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.6250000000000002e-05,
      "loss": 2.4506,
      "step": 949
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.6214285714285714e-05,
      "loss": 2.5834,
      "step": 950
    },
    {
      "epoch": 1.36,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.337965488433838,
      "eval_runtime": 74.0169,
      "eval_samples_per_second": 3.148,
      "eval_steps_per_second": 1.581,
      "step": 950
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.617857142857143e-05,
      "loss": 2.4535,
      "step": 951
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.614285714285714e-05,
      "loss": 2.4144,
      "step": 952
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.6107142857142857e-05,
      "loss": 2.2113,
      "step": 953
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.6071428571428572e-05,
      "loss": 2.7915,
      "step": 954
    },
    {
      "epoch": 1.36,
      "learning_rate": 1.6035714285714287e-05,
      "loss": 2.3815,
      "step": 955
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.6000000000000003e-05,
      "loss": 2.1403,
      "step": 956
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.5964285714285715e-05,
      "loss": 2.4865,
      "step": 957
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.592857142857143e-05,
      "loss": 2.4652,
      "step": 958
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.5892857142857142e-05,
      "loss": 2.2944,
      "step": 959
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.5857142857142857e-05,
      "loss": 2.3786,
      "step": 960
    },
    {
      "epoch": 1.37,
      "eval_cer": 0.9705335810990178,
      "eval_loss": 2.341917037963867,
      "eval_runtime": 71.0003,
      "eval_samples_per_second": 3.282,
      "eval_steps_per_second": 1.648,
      "step": 960
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.5821428571428573e-05,
      "loss": 2.4706,
      "step": 961
    },
    {
      "epoch": 1.37,
      "learning_rate": 1.5785714285714288e-05,
      "loss": 2.3035,
      "step": 962
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.575e-05,
      "loss": 2.4327,
      "step": 963
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5714285714285715e-05,
      "loss": 2.4158,
      "step": 964
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5678571428571427e-05,
      "loss": 2.2634,
      "step": 965
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5642857142857143e-05,
      "loss": 2.579,
      "step": 966
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5607142857142858e-05,
      "loss": 2.5682,
      "step": 967
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5571428571428573e-05,
      "loss": 2.2377,
      "step": 968
    },
    {
      "epoch": 1.38,
      "learning_rate": 1.5535714285714285e-05,
      "loss": 2.3291,
      "step": 969
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.55e-05,
      "loss": 2.3477,
      "step": 970
    },
    {
      "epoch": 1.39,
      "eval_cer": 0.9730554818157685,
      "eval_loss": 2.326253652572632,
      "eval_runtime": 73.3276,
      "eval_samples_per_second": 3.178,
      "eval_steps_per_second": 1.596,
      "step": 970
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.5464285714285716e-05,
      "loss": 2.233,
      "step": 971
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.5428571428571428e-05,
      "loss": 2.4289,
      "step": 972
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.5392857142857143e-05,
      "loss": 2.3164,
      "step": 973
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.535714285714286e-05,
      "loss": 2.3791,
      "step": 974
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.5321428571428574e-05,
      "loss": 2.4563,
      "step": 975
    },
    {
      "epoch": 1.39,
      "learning_rate": 1.5285714285714286e-05,
      "loss": 2.2284,
      "step": 976
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.525e-05,
      "loss": 2.6288,
      "step": 977
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.5214285714285715e-05,
      "loss": 2.2246,
      "step": 978
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.5178571428571429e-05,
      "loss": 2.1509,
      "step": 979
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.5142857142857144e-05,
      "loss": 2.5044,
      "step": 980
    },
    {
      "epoch": 1.4,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.344243288040161,
      "eval_runtime": 75.154,
      "eval_samples_per_second": 3.1,
      "eval_steps_per_second": 1.557,
      "step": 980
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.510714285714286e-05,
      "loss": 2.117,
      "step": 981
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.5071428571428573e-05,
      "loss": 2.2873,
      "step": 982
    },
    {
      "epoch": 1.4,
      "learning_rate": 1.5035714285714287e-05,
      "loss": 2.4189,
      "step": 983
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.5e-05,
      "loss": 2.1279,
      "step": 984
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4964285714285714e-05,
      "loss": 2.3338,
      "step": 985
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4928571428571431e-05,
      "loss": 2.2194,
      "step": 986
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4892857142857145e-05,
      "loss": 2.1962,
      "step": 987
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4857142857142858e-05,
      "loss": 2.0866,
      "step": 988
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4821428571428572e-05,
      "loss": 2.3401,
      "step": 989
    },
    {
      "epoch": 1.41,
      "learning_rate": 1.4785714285714286e-05,
      "loss": 2.4569,
      "step": 990
    },
    {
      "epoch": 1.41,
      "eval_cer": 0.9741173347491372,
      "eval_loss": 2.3430724143981934,
      "eval_runtime": 72.6823,
      "eval_samples_per_second": 3.206,
      "eval_steps_per_second": 1.61,
      "step": 990
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.475e-05,
      "loss": 2.3355,
      "step": 991
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.4714285714285713e-05,
      "loss": 2.2955,
      "step": 992
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.467857142857143e-05,
      "loss": 2.4514,
      "step": 993
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.4642857142857144e-05,
      "loss": 2.425,
      "step": 994
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.4607142857142857e-05,
      "loss": 2.5071,
      "step": 995
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.4571428571428573e-05,
      "loss": 2.3321,
      "step": 996
    },
    {
      "epoch": 1.42,
      "learning_rate": 1.4535714285714286e-05,
      "loss": 2.6415,
      "step": 997
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.45e-05,
      "loss": 2.3443,
      "step": 998
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.4464285714285717e-05,
      "loss": 2.2536,
      "step": 999
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.442857142857143e-05,
      "loss": 2.1939,
      "step": 1000
    },
    {
      "epoch": 1.43,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3410563468933105,
      "eval_runtime": 72.7941,
      "eval_samples_per_second": 3.201,
      "eval_steps_per_second": 1.607,
      "step": 1000
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.4392857142857144e-05,
      "loss": 2.4073,
      "step": 1001
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.4357142857142858e-05,
      "loss": 2.441,
      "step": 1002
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.4321428571428572e-05,
      "loss": 2.4092,
      "step": 1003
    },
    {
      "epoch": 1.43,
      "learning_rate": 1.4285714285714285e-05,
      "loss": 2.674,
      "step": 1004
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.4249999999999999e-05,
      "loss": 2.372,
      "step": 1005
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.4214285714285716e-05,
      "loss": 2.3776,
      "step": 1006
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.417857142857143e-05,
      "loss": 2.1772,
      "step": 1007
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.4142857142857143e-05,
      "loss": 2.3794,
      "step": 1008
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.4107142857142857e-05,
      "loss": 2.5189,
      "step": 1009
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.407142857142857e-05,
      "loss": 2.3233,
      "step": 1010
    },
    {
      "epoch": 1.44,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.312274694442749,
      "eval_runtime": 74.6029,
      "eval_samples_per_second": 3.123,
      "eval_steps_per_second": 1.568,
      "step": 1010
    },
    {
      "epoch": 1.44,
      "learning_rate": 1.4035714285714286e-05,
      "loss": 2.1249,
      "step": 1011
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.4000000000000001e-05,
      "loss": 2.1775,
      "step": 1012
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.3964285714285715e-05,
      "loss": 2.5601,
      "step": 1013
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.392857142857143e-05,
      "loss": 2.3522,
      "step": 1014
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.3892857142857144e-05,
      "loss": 2.2378,
      "step": 1015
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.3857142857142858e-05,
      "loss": 2.2242,
      "step": 1016
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.3821428571428571e-05,
      "loss": 2.2404,
      "step": 1017
    },
    {
      "epoch": 1.45,
      "learning_rate": 1.3785714285714285e-05,
      "loss": 2.3337,
      "step": 1018
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.3750000000000002e-05,
      "loss": 2.3727,
      "step": 1019
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.3714285714285716e-05,
      "loss": 2.3079,
      "step": 1020
    },
    {
      "epoch": 1.46,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3085997104644775,
      "eval_runtime": 75.2826,
      "eval_samples_per_second": 3.095,
      "eval_steps_per_second": 1.554,
      "step": 1020
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.367857142857143e-05,
      "loss": 3.0099,
      "step": 1021
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.3642857142857143e-05,
      "loss": 2.4151,
      "step": 1022
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.3607142857142857e-05,
      "loss": 2.2172,
      "step": 1023
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.357142857142857e-05,
      "loss": 2.336,
      "step": 1024
    },
    {
      "epoch": 1.46,
      "learning_rate": 1.3535714285714288e-05,
      "loss": 2.2692,
      "step": 1025
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3500000000000001e-05,
      "loss": 2.4067,
      "step": 1026
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3464285714285715e-05,
      "loss": 2.2447,
      "step": 1027
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3428571428571429e-05,
      "loss": 2.5013,
      "step": 1028
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3392857142857144e-05,
      "loss": 2.3684,
      "step": 1029
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3357142857142858e-05,
      "loss": 2.2933,
      "step": 1030
    },
    {
      "epoch": 1.47,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.310109853744507,
      "eval_runtime": 73.8146,
      "eval_samples_per_second": 3.157,
      "eval_steps_per_second": 1.585,
      "step": 1030
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3321428571428571e-05,
      "loss": 2.3025,
      "step": 1031
    },
    {
      "epoch": 1.47,
      "learning_rate": 1.3285714285714288e-05,
      "loss": 2.4556,
      "step": 1032
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3250000000000002e-05,
      "loss": 2.2622,
      "step": 1033
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3214285714285716e-05,
      "loss": 2.3974,
      "step": 1034
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.317857142857143e-05,
      "loss": 2.191,
      "step": 1035
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3142857142857143e-05,
      "loss": 2.5816,
      "step": 1036
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3107142857142857e-05,
      "loss": 2.1219,
      "step": 1037
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3071428571428574e-05,
      "loss": 2.2479,
      "step": 1038
    },
    {
      "epoch": 1.48,
      "learning_rate": 1.3035714285714287e-05,
      "loss": 2.2505,
      "step": 1039
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.3000000000000001e-05,
      "loss": 2.1207,
      "step": 1040
    },
    {
      "epoch": 1.49,
      "eval_cer": 0.9482346694982745,
      "eval_loss": 2.3153793811798096,
      "eval_runtime": 76.0702,
      "eval_samples_per_second": 3.063,
      "eval_steps_per_second": 1.538,
      "step": 1040
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2964285714285715e-05,
      "loss": 2.5858,
      "step": 1041
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2928571428571428e-05,
      "loss": 2.634,
      "step": 1042
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2892857142857142e-05,
      "loss": 2.5861,
      "step": 1043
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2857142857142857e-05,
      "loss": 2.612,
      "step": 1044
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2821428571428573e-05,
      "loss": 2.1324,
      "step": 1045
    },
    {
      "epoch": 1.49,
      "learning_rate": 1.2785714285714286e-05,
      "loss": 2.1726,
      "step": 1046
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2750000000000002e-05,
      "loss": 2.2977,
      "step": 1047
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2714285714285715e-05,
      "loss": 2.2068,
      "step": 1048
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2678571428571429e-05,
      "loss": 2.2691,
      "step": 1049
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2642857142857143e-05,
      "loss": 2.3353,
      "step": 1050
    },
    {
      "epoch": 1.5,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.306945562362671,
      "eval_runtime": 70.6853,
      "eval_samples_per_second": 3.296,
      "eval_steps_per_second": 1.655,
      "step": 1050
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.260714285714286e-05,
      "loss": 2.578,
      "step": 1051
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2571428571428573e-05,
      "loss": 2.6019,
      "step": 1052
    },
    {
      "epoch": 1.5,
      "learning_rate": 1.2535714285714287e-05,
      "loss": 2.0848,
      "step": 1053
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.25e-05,
      "loss": 2.4074,
      "step": 1054
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.2464285714285714e-05,
      "loss": 2.179,
      "step": 1055
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.242857142857143e-05,
      "loss": 2.3035,
      "step": 1056
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.2392857142857143e-05,
      "loss": 2.2438,
      "step": 1057
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.2357142857142857e-05,
      "loss": 2.0885,
      "step": 1058
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.2321428571428572e-05,
      "loss": 2.4772,
      "step": 1059
    },
    {
      "epoch": 1.51,
      "learning_rate": 1.2285714285714286e-05,
      "loss": 2.3848,
      "step": 1060
    },
    {
      "epoch": 1.51,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.309279441833496,
      "eval_runtime": 73.5559,
      "eval_samples_per_second": 3.168,
      "eval_steps_per_second": 1.591,
      "step": 1060
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.225e-05,
      "loss": 2.2509,
      "step": 1061
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2214285714285715e-05,
      "loss": 2.3144,
      "step": 1062
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2178571428571429e-05,
      "loss": 2.4631,
      "step": 1063
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2142857142857144e-05,
      "loss": 2.2754,
      "step": 1064
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2107142857142858e-05,
      "loss": 2.7208,
      "step": 1065
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2071428571428573e-05,
      "loss": 2.2386,
      "step": 1066
    },
    {
      "epoch": 1.52,
      "learning_rate": 1.2035714285714287e-05,
      "loss": 1.9774,
      "step": 1067
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.2e-05,
      "loss": 2.6847,
      "step": 1068
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.1964285714285716e-05,
      "loss": 2.5572,
      "step": 1069
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.192857142857143e-05,
      "loss": 2.1241,
      "step": 1070
    },
    {
      "epoch": 1.53,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.3012731075286865,
      "eval_runtime": 77.9424,
      "eval_samples_per_second": 2.989,
      "eval_steps_per_second": 1.501,
      "step": 1070
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.1892857142857143e-05,
      "loss": 2.4037,
      "step": 1071
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.1857142857142858e-05,
      "loss": 2.41,
      "step": 1072
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.1821428571428572e-05,
      "loss": 2.5481,
      "step": 1073
    },
    {
      "epoch": 1.53,
      "learning_rate": 1.1785714285714286e-05,
      "loss": 2.3584,
      "step": 1074
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.175e-05,
      "loss": 2.3838,
      "step": 1075
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1714285714285715e-05,
      "loss": 2.1845,
      "step": 1076
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1678571428571428e-05,
      "loss": 2.4537,
      "step": 1077
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1642857142857144e-05,
      "loss": 2.1782,
      "step": 1078
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1607142857142857e-05,
      "loss": 2.392,
      "step": 1079
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1571428571428573e-05,
      "loss": 2.5261,
      "step": 1080
    },
    {
      "epoch": 1.54,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.311267137527466,
      "eval_runtime": 75.0491,
      "eval_samples_per_second": 3.105,
      "eval_steps_per_second": 1.559,
      "step": 1080
    },
    {
      "epoch": 1.54,
      "learning_rate": 1.1535714285714286e-05,
      "loss": 2.3837,
      "step": 1081
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1500000000000002e-05,
      "loss": 2.3387,
      "step": 1082
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1464285714285715e-05,
      "loss": 2.6537,
      "step": 1083
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1428571428571429e-05,
      "loss": 2.5084,
      "step": 1084
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1392857142857144e-05,
      "loss": 2.5444,
      "step": 1085
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1357142857142858e-05,
      "loss": 2.3173,
      "step": 1086
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1321428571428572e-05,
      "loss": 2.3751,
      "step": 1087
    },
    {
      "epoch": 1.55,
      "learning_rate": 1.1285714285714285e-05,
      "loss": 2.3343,
      "step": 1088
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.125e-05,
      "loss": 2.5928,
      "step": 1089
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.1214285714285714e-05,
      "loss": 2.5784,
      "step": 1090
    },
    {
      "epoch": 1.56,
      "eval_cer": 0.9743827979824794,
      "eval_loss": 2.300593376159668,
      "eval_runtime": 70.7133,
      "eval_samples_per_second": 3.295,
      "eval_steps_per_second": 1.655,
      "step": 1090
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.1178571428571428e-05,
      "loss": 2.4525,
      "step": 1091
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.1142857142857143e-05,
      "loss": 2.8449,
      "step": 1092
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.1107142857142857e-05,
      "loss": 2.3599,
      "step": 1093
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.107142857142857e-05,
      "loss": 2.4282,
      "step": 1094
    },
    {
      "epoch": 1.56,
      "learning_rate": 1.1035714285714286e-05,
      "loss": 2.4416,
      "step": 1095
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.1000000000000001e-05,
      "loss": 2.1889,
      "step": 1096
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.0964285714285715e-05,
      "loss": 2.2039,
      "step": 1097
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.092857142857143e-05,
      "loss": 2.2238,
      "step": 1098
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.0892857142857144e-05,
      "loss": 2.3799,
      "step": 1099
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.0857142857142858e-05,
      "loss": 2.2218,
      "step": 1100
    },
    {
      "epoch": 1.57,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.293494701385498,
      "eval_runtime": 72.4661,
      "eval_samples_per_second": 3.215,
      "eval_steps_per_second": 1.615,
      "step": 1100
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.0821428571428573e-05,
      "loss": 2.4075,
      "step": 1101
    },
    {
      "epoch": 1.57,
      "learning_rate": 1.0785714285714287e-05,
      "loss": 2.4006,
      "step": 1102
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.075e-05,
      "loss": 2.1987,
      "step": 1103
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.0714285714285714e-05,
      "loss": 2.2783,
      "step": 1104
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.067857142857143e-05,
      "loss": 2.5578,
      "step": 1105
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.0642857142857143e-05,
      "loss": 2.4563,
      "step": 1106
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.0607142857142857e-05,
      "loss": 2.4099,
      "step": 1107
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.0571428571428572e-05,
      "loss": 2.347,
      "step": 1108
    },
    {
      "epoch": 1.58,
      "learning_rate": 1.0535714285714286e-05,
      "loss": 2.2402,
      "step": 1109
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.05e-05,
      "loss": 2.4242,
      "step": 1110
    },
    {
      "epoch": 1.59,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2985830307006836,
      "eval_runtime": 74.2439,
      "eval_samples_per_second": 3.138,
      "eval_steps_per_second": 1.576,
      "step": 1110
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0464285714285715e-05,
      "loss": 2.4298,
      "step": 1111
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0428571428571428e-05,
      "loss": 2.3271,
      "step": 1112
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0392857142857144e-05,
      "loss": 2.0553,
      "step": 1113
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0357142857142859e-05,
      "loss": 2.0748,
      "step": 1114
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0321428571428573e-05,
      "loss": 2.3834,
      "step": 1115
    },
    {
      "epoch": 1.59,
      "learning_rate": 1.0285714285714286e-05,
      "loss": 2.7342,
      "step": 1116
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.025e-05,
      "loss": 2.718,
      "step": 1117
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0214285714285715e-05,
      "loss": 2.4485,
      "step": 1118
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0178571428571429e-05,
      "loss": 2.4851,
      "step": 1119
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0142857142857143e-05,
      "loss": 2.4834,
      "step": 1120
    },
    {
      "epoch": 1.6,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.306148052215576,
      "eval_runtime": 74.4231,
      "eval_samples_per_second": 3.131,
      "eval_steps_per_second": 1.572,
      "step": 1120
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0107142857142858e-05,
      "loss": 2.1025,
      "step": 1121
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0071428571428572e-05,
      "loss": 2.2103,
      "step": 1122
    },
    {
      "epoch": 1.6,
      "learning_rate": 1.0035714285714285e-05,
      "loss": 2.2687,
      "step": 1123
    },
    {
      "epoch": 1.61,
      "learning_rate": 1e-05,
      "loss": 2.3822,
      "step": 1124
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.964285714285714e-06,
      "loss": 2.3551,
      "step": 1125
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.928571428571428e-06,
      "loss": 2.3252,
      "step": 1126
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.892857142857143e-06,
      "loss": 2.3465,
      "step": 1127
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.857142857142857e-06,
      "loss": 2.6682,
      "step": 1128
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.821428571428573e-06,
      "loss": 2.3561,
      "step": 1129
    },
    {
      "epoch": 1.61,
      "learning_rate": 9.785714285714286e-06,
      "loss": 2.1548,
      "step": 1130
    },
    {
      "epoch": 1.61,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2904534339904785,
      "eval_runtime": 79.2073,
      "eval_samples_per_second": 2.942,
      "eval_steps_per_second": 1.477,
      "step": 1130
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.750000000000002e-06,
      "loss": 2.3771,
      "step": 1131
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.714285714285715e-06,
      "loss": 2.3255,
      "step": 1132
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.678571428571429e-06,
      "loss": 2.2943,
      "step": 1133
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.642857142857144e-06,
      "loss": 2.2061,
      "step": 1134
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.607142857142858e-06,
      "loss": 2.3374,
      "step": 1135
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.571428571428572e-06,
      "loss": 2.3975,
      "step": 1136
    },
    {
      "epoch": 1.62,
      "learning_rate": 9.535714285714287e-06,
      "loss": 2.4614,
      "step": 1137
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.5e-06,
      "loss": 2.2331,
      "step": 1138
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.464285714285714e-06,
      "loss": 2.2732,
      "step": 1139
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.42857142857143e-06,
      "loss": 2.2794,
      "step": 1140
    },
    {
      "epoch": 1.63,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2776906490325928,
      "eval_runtime": 72.731,
      "eval_samples_per_second": 3.204,
      "eval_steps_per_second": 1.609,
      "step": 1140
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.392857142857143e-06,
      "loss": 2.4457,
      "step": 1141
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.357142857142857e-06,
      "loss": 2.3159,
      "step": 1142
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.32142857142857e-06,
      "loss": 2.218,
      "step": 1143
    },
    {
      "epoch": 1.63,
      "learning_rate": 9.285714285714286e-06,
      "loss": 2.329,
      "step": 1144
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.25e-06,
      "loss": 2.2833,
      "step": 1145
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.214285714285715e-06,
      "loss": 2.5647,
      "step": 1146
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.17857142857143e-06,
      "loss": 2.02,
      "step": 1147
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.142857142857144e-06,
      "loss": 2.1038,
      "step": 1148
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.107142857142858e-06,
      "loss": 2.0677,
      "step": 1149
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.071428571428573e-06,
      "loss": 2.1035,
      "step": 1150
    },
    {
      "epoch": 1.64,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2948994636535645,
      "eval_runtime": 75.8603,
      "eval_samples_per_second": 3.071,
      "eval_steps_per_second": 1.542,
      "step": 1150
    },
    {
      "epoch": 1.64,
      "learning_rate": 9.035714285714287e-06,
      "loss": 2.3401,
      "step": 1151
    },
    {
      "epoch": 1.65,
      "learning_rate": 9e-06,
      "loss": 2.1931,
      "step": 1152
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.964285714285716e-06,
      "loss": 2.4197,
      "step": 1153
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.92857142857143e-06,
      "loss": 2.684,
      "step": 1154
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.892857142857143e-06,
      "loss": 2.4692,
      "step": 1155
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.857142857142857e-06,
      "loss": 2.0308,
      "step": 1156
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.821428571428572e-06,
      "loss": 2.3805,
      "step": 1157
    },
    {
      "epoch": 1.65,
      "learning_rate": 8.785714285714286e-06,
      "loss": 2.1279,
      "step": 1158
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.75e-06,
      "loss": 2.5567,
      "step": 1159
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.714285714285715e-06,
      "loss": 2.8296,
      "step": 1160
    },
    {
      "epoch": 1.66,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.271817684173584,
      "eval_runtime": 72.944,
      "eval_samples_per_second": 3.194,
      "eval_steps_per_second": 1.604,
      "step": 1160
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.678571428571428e-06,
      "loss": 2.1915,
      "step": 1161
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.642857142857144e-06,
      "loss": 2.5226,
      "step": 1162
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.607142857142857e-06,
      "loss": 2.2844,
      "step": 1163
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.571428571428573e-06,
      "loss": 2.3728,
      "step": 1164
    },
    {
      "epoch": 1.66,
      "learning_rate": 8.535714285714286e-06,
      "loss": 2.1984,
      "step": 1165
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.500000000000002e-06,
      "loss": 2.3736,
      "step": 1166
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.464285714285715e-06,
      "loss": 2.2721,
      "step": 1167
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.428571428571429e-06,
      "loss": 2.2548,
      "step": 1168
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.392857142857143e-06,
      "loss": 2.757,
      "step": 1169
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.357142857142858e-06,
      "loss": 2.4334,
      "step": 1170
    },
    {
      "epoch": 1.67,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.278010129928589,
      "eval_runtime": 71.7945,
      "eval_samples_per_second": 3.245,
      "eval_steps_per_second": 1.63,
      "step": 1170
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.321428571428572e-06,
      "loss": 2.3181,
      "step": 1171
    },
    {
      "epoch": 1.67,
      "learning_rate": 8.285714285714285e-06,
      "loss": 2.2391,
      "step": 1172
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.25e-06,
      "loss": 2.4014,
      "step": 1173
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.214285714285714e-06,
      "loss": 2.4148,
      "step": 1174
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.178571428571428e-06,
      "loss": 2.1601,
      "step": 1175
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.142857142857143e-06,
      "loss": 2.5704,
      "step": 1176
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.107142857142857e-06,
      "loss": 2.2524,
      "step": 1177
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.07142857142857e-06,
      "loss": 2.1132,
      "step": 1178
    },
    {
      "epoch": 1.68,
      "learning_rate": 8.035714285714286e-06,
      "loss": 2.6925,
      "step": 1179
    },
    {
      "epoch": 1.69,
      "learning_rate": 8.000000000000001e-06,
      "loss": 2.4546,
      "step": 1180
    },
    {
      "epoch": 1.69,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.277035713195801,
      "eval_runtime": 71.7973,
      "eval_samples_per_second": 3.245,
      "eval_steps_per_second": 1.63,
      "step": 1180
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.964285714285715e-06,
      "loss": 2.5919,
      "step": 1181
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.928571428571429e-06,
      "loss": 2.277,
      "step": 1182
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.892857142857144e-06,
      "loss": 2.1411,
      "step": 1183
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.857142857142858e-06,
      "loss": 2.3251,
      "step": 1184
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.821428571428571e-06,
      "loss": 2.0189,
      "step": 1185
    },
    {
      "epoch": 1.69,
      "learning_rate": 7.785714285714287e-06,
      "loss": 2.2687,
      "step": 1186
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.75e-06,
      "loss": 2.5713,
      "step": 1187
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.714285714285714e-06,
      "loss": 1.8063,
      "step": 1188
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.67857142857143e-06,
      "loss": 2.2335,
      "step": 1189
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.642857142857143e-06,
      "loss": 2.507,
      "step": 1190
    },
    {
      "epoch": 1.7,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.266570568084717,
      "eval_runtime": 68.8985,
      "eval_samples_per_second": 3.382,
      "eval_steps_per_second": 1.698,
      "step": 1190
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.6071428571428575e-06,
      "loss": 2.3437,
      "step": 1191
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.571428571428572e-06,
      "loss": 2.0907,
      "step": 1192
    },
    {
      "epoch": 1.7,
      "learning_rate": 7.5357142857142865e-06,
      "loss": 2.5063,
      "step": 1193
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.5e-06,
      "loss": 2.6549,
      "step": 1194
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.4642857142857155e-06,
      "loss": 2.3958,
      "step": 1195
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.428571428571429e-06,
      "loss": 2.2524,
      "step": 1196
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.392857142857143e-06,
      "loss": 2.307,
      "step": 1197
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.3571428571428565e-06,
      "loss": 2.4221,
      "step": 1198
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.321428571428572e-06,
      "loss": 2.6643,
      "step": 1199
    },
    {
      "epoch": 1.71,
      "learning_rate": 7.285714285714286e-06,
      "loss": 2.2962,
      "step": 1200
    },
    {
      "epoch": 1.71,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.272502899169922,
      "eval_runtime": 76.3915,
      "eval_samples_per_second": 3.05,
      "eval_steps_per_second": 1.532,
      "step": 1200
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.25e-06,
      "loss": 2.3814,
      "step": 1201
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.214285714285715e-06,
      "loss": 2.2412,
      "step": 1202
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.178571428571429e-06,
      "loss": 2.4362,
      "step": 1203
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.142857142857143e-06,
      "loss": 2.3845,
      "step": 1204
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.107142857142858e-06,
      "loss": 2.5904,
      "step": 1205
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.071428571428572e-06,
      "loss": 2.1527,
      "step": 1206
    },
    {
      "epoch": 1.72,
      "learning_rate": 7.035714285714285e-06,
      "loss": 2.3925,
      "step": 1207
    },
    {
      "epoch": 1.73,
      "learning_rate": 7.000000000000001e-06,
      "loss": 2.2432,
      "step": 1208
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.964285714285715e-06,
      "loss": 2.2131,
      "step": 1209
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.928571428571429e-06,
      "loss": 2.2345,
      "step": 1210
    },
    {
      "epoch": 1.73,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.269658088684082,
      "eval_runtime": 70.846,
      "eval_samples_per_second": 3.289,
      "eval_steps_per_second": 1.651,
      "step": 1210
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.8928571428571426e-06,
      "loss": 2.1864,
      "step": 1211
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.857142857142858e-06,
      "loss": 2.2897,
      "step": 1212
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.821428571428572e-06,
      "loss": 2.1784,
      "step": 1213
    },
    {
      "epoch": 1.73,
      "learning_rate": 6.785714285714285e-06,
      "loss": 2.4477,
      "step": 1214
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.750000000000001e-06,
      "loss": 2.2971,
      "step": 1215
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.714285714285714e-06,
      "loss": 2.3651,
      "step": 1216
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.678571428571429e-06,
      "loss": 2.2919,
      "step": 1217
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.642857142857144e-06,
      "loss": 2.2171,
      "step": 1218
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.607142857142858e-06,
      "loss": 2.3895,
      "step": 1219
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.5714285714285714e-06,
      "loss": 2.3129,
      "step": 1220
    },
    {
      "epoch": 1.74,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2695419788360596,
      "eval_runtime": 73.1793,
      "eval_samples_per_second": 3.184,
      "eval_steps_per_second": 1.599,
      "step": 1220
    },
    {
      "epoch": 1.74,
      "learning_rate": 6.535714285714287e-06,
      "loss": 2.4243,
      "step": 1221
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.5000000000000004e-06,
      "loss": 2.5857,
      "step": 1222
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.464285714285714e-06,
      "loss": 2.6617,
      "step": 1223
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.428571428571429e-06,
      "loss": 2.6073,
      "step": 1224
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.392857142857143e-06,
      "loss": 2.0906,
      "step": 1225
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.357142857142858e-06,
      "loss": 2.3422,
      "step": 1226
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.321428571428571e-06,
      "loss": 2.7439,
      "step": 1227
    },
    {
      "epoch": 1.75,
      "learning_rate": 6.285714285714287e-06,
      "loss": 2.1941,
      "step": 1228
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.25e-06,
      "loss": 2.4268,
      "step": 1229
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.214285714285715e-06,
      "loss": 2.2666,
      "step": 1230
    },
    {
      "epoch": 1.76,
      "eval_cer": 0.9709981417573667,
      "eval_loss": 2.2696316242218018,
      "eval_runtime": 70.1039,
      "eval_samples_per_second": 3.324,
      "eval_steps_per_second": 1.669,
      "step": 1230
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.1785714285714285e-06,
      "loss": 2.4667,
      "step": 1231
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.142857142857143e-06,
      "loss": 2.3757,
      "step": 1232
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.1071428571428575e-06,
      "loss": 2.568,
      "step": 1233
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.071428571428572e-06,
      "loss": 2.2628,
      "step": 1234
    },
    {
      "epoch": 1.76,
      "learning_rate": 6.0357142857142865e-06,
      "loss": 2.4575,
      "step": 1235
    },
    {
      "epoch": 1.77,
      "learning_rate": 6e-06,
      "loss": 2.0919,
      "step": 1236
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.964285714285715e-06,
      "loss": 2.0899,
      "step": 1237
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.928571428571429e-06,
      "loss": 2.3788,
      "step": 1238
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.892857142857143e-06,
      "loss": 2.2975,
      "step": 1239
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.857142857142857e-06,
      "loss": 2.6001,
      "step": 1240
    },
    {
      "epoch": 1.77,
      "eval_cer": 0.9730554818157685,
      "eval_loss": 2.2504379749298096,
      "eval_runtime": 71.2108,
      "eval_samples_per_second": 3.272,
      "eval_steps_per_second": 1.643,
      "step": 1240
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.821428571428572e-06,
      "loss": 2.4764,
      "step": 1241
    },
    {
      "epoch": 1.77,
      "learning_rate": 5.785714285714286e-06,
      "loss": 2.2776,
      "step": 1242
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.750000000000001e-06,
      "loss": 2.3125,
      "step": 1243
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.7142857142857145e-06,
      "loss": 2.3827,
      "step": 1244
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.678571428571429e-06,
      "loss": 2.3836,
      "step": 1245
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.642857142857143e-06,
      "loss": 1.996,
      "step": 1246
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.607142857142857e-06,
      "loss": 2.3332,
      "step": 1247
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.571428571428572e-06,
      "loss": 2.3485,
      "step": 1248
    },
    {
      "epoch": 1.78,
      "learning_rate": 5.535714285714285e-06,
      "loss": 2.205,
      "step": 1249
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.500000000000001e-06,
      "loss": 2.4457,
      "step": 1250
    },
    {
      "epoch": 1.79,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2474441528320312,
      "eval_runtime": 70.5582,
      "eval_samples_per_second": 3.302,
      "eval_steps_per_second": 1.658,
      "step": 1250
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.464285714285715e-06,
      "loss": 2.2247,
      "step": 1251
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.428571428571429e-06,
      "loss": 2.2986,
      "step": 1252
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.392857142857143e-06,
      "loss": 2.3671,
      "step": 1253
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.357142857142857e-06,
      "loss": 2.2226,
      "step": 1254
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.3214285714285715e-06,
      "loss": 2.5368,
      "step": 1255
    },
    {
      "epoch": 1.79,
      "learning_rate": 5.285714285714286e-06,
      "loss": 2.4053,
      "step": 1256
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.25e-06,
      "loss": 2.1863,
      "step": 1257
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.214285714285714e-06,
      "loss": 2.2022,
      "step": 1258
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.1785714285714296e-06,
      "loss": 2.217,
      "step": 1259
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.142857142857143e-06,
      "loss": 2.224,
      "step": 1260
    },
    {
      "epoch": 1.8,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2488021850585938,
      "eval_runtime": 70.9487,
      "eval_samples_per_second": 3.284,
      "eval_steps_per_second": 1.649,
      "step": 1260
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.107142857142858e-06,
      "loss": 2.0988,
      "step": 1261
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.071428571428571e-06,
      "loss": 2.2568,
      "step": 1262
    },
    {
      "epoch": 1.8,
      "learning_rate": 5.035714285714286e-06,
      "loss": 2.2597,
      "step": 1263
    },
    {
      "epoch": 1.81,
      "learning_rate": 5e-06,
      "loss": 2.3695,
      "step": 1264
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.964285714285714e-06,
      "loss": 2.1682,
      "step": 1265
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.9285714285714286e-06,
      "loss": 1.9801,
      "step": 1266
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.892857142857143e-06,
      "loss": 2.4685,
      "step": 1267
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.857142857142858e-06,
      "loss": 2.2281,
      "step": 1268
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.821428571428572e-06,
      "loss": 2.4883,
      "step": 1269
    },
    {
      "epoch": 1.81,
      "learning_rate": 4.785714285714286e-06,
      "loss": 2.3024,
      "step": 1270
    },
    {
      "epoch": 1.81,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.252497911453247,
      "eval_runtime": 74.7566,
      "eval_samples_per_second": 3.117,
      "eval_steps_per_second": 1.565,
      "step": 1270
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.75e-06,
      "loss": 2.23,
      "step": 1271
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.714285714285715e-06,
      "loss": 2.076,
      "step": 1272
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.6785714285714284e-06,
      "loss": 2.4412,
      "step": 1273
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.642857142857143e-06,
      "loss": 2.2819,
      "step": 1274
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.6071428571428574e-06,
      "loss": 2.9874,
      "step": 1275
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.571428571428572e-06,
      "loss": 2.2238,
      "step": 1276
    },
    {
      "epoch": 1.82,
      "learning_rate": 4.5357142857142865e-06,
      "loss": 2.3396,
      "step": 1277
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.5e-06,
      "loss": 2.1018,
      "step": 1278
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.464285714285715e-06,
      "loss": 2.4404,
      "step": 1279
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.428571428571428e-06,
      "loss": 2.2811,
      "step": 1280
    },
    {
      "epoch": 1.83,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.25191068649292,
      "eval_runtime": 68.1989,
      "eval_samples_per_second": 3.416,
      "eval_steps_per_second": 1.716,
      "step": 1280
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.392857142857143e-06,
      "loss": 2.38,
      "step": 1281
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.357142857142857e-06,
      "loss": 2.1465,
      "step": 1282
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.321428571428572e-06,
      "loss": 2.198,
      "step": 1283
    },
    {
      "epoch": 1.83,
      "learning_rate": 4.285714285714286e-06,
      "loss": 2.1484,
      "step": 1284
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.250000000000001e-06,
      "loss": 2.3102,
      "step": 1285
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.2142857142857145e-06,
      "loss": 2.2106,
      "step": 1286
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.178571428571429e-06,
      "loss": 2.0874,
      "step": 1287
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.142857142857143e-06,
      "loss": 2.6193,
      "step": 1288
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.107142857142857e-06,
      "loss": 2.1307,
      "step": 1289
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.071428571428572e-06,
      "loss": 2.3398,
      "step": 1290
    },
    {
      "epoch": 1.84,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.246530055999756,
      "eval_runtime": 74.6949,
      "eval_samples_per_second": 3.119,
      "eval_steps_per_second": 1.566,
      "step": 1290
    },
    {
      "epoch": 1.84,
      "learning_rate": 4.035714285714285e-06,
      "loss": 2.2889,
      "step": 1291
    },
    {
      "epoch": 1.85,
      "learning_rate": 4.000000000000001e-06,
      "loss": 2.0118,
      "step": 1292
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.964285714285714e-06,
      "loss": 2.3003,
      "step": 1293
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.928571428571429e-06,
      "loss": 2.1563,
      "step": 1294
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.892857142857143e-06,
      "loss": 2.1969,
      "step": 1295
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.857142857142857e-06,
      "loss": 2.2539,
      "step": 1296
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.8214285714285715e-06,
      "loss": 2.1096,
      "step": 1297
    },
    {
      "epoch": 1.85,
      "learning_rate": 3.785714285714286e-06,
      "loss": 2.3241,
      "step": 1298
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.75e-06,
      "loss": 2.2204,
      "step": 1299
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.7142857142857146e-06,
      "loss": 2.1662,
      "step": 1300
    },
    {
      "epoch": 1.86,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.245842456817627,
      "eval_runtime": 74.4603,
      "eval_samples_per_second": 3.129,
      "eval_steps_per_second": 1.571,
      "step": 1300
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.6785714285714283e-06,
      "loss": 2.4916,
      "step": 1301
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.642857142857143e-06,
      "loss": 2.1858,
      "step": 1302
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.6071428571428577e-06,
      "loss": 2.3599,
      "step": 1303
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.5714285714285714e-06,
      "loss": 2.164,
      "step": 1304
    },
    {
      "epoch": 1.86,
      "learning_rate": 3.535714285714286e-06,
      "loss": 2.2529,
      "step": 1305
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.5000000000000004e-06,
      "loss": 2.2876,
      "step": 1306
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.4642857142857145e-06,
      "loss": 2.3625,
      "step": 1307
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.428571428571429e-06,
      "loss": 2.2858,
      "step": 1308
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.3928571428571426e-06,
      "loss": 2.1749,
      "step": 1309
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.357142857142857e-06,
      "loss": 2.5555,
      "step": 1310
    },
    {
      "epoch": 1.87,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.245615005493164,
      "eval_runtime": 74.7468,
      "eval_samples_per_second": 3.117,
      "eval_steps_per_second": 1.565,
      "step": 1310
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.321428571428572e-06,
      "loss": 2.2155,
      "step": 1311
    },
    {
      "epoch": 1.87,
      "learning_rate": 3.2857142857142857e-06,
      "loss": 2.2056,
      "step": 1312
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.2500000000000002e-06,
      "loss": 2.3531,
      "step": 1313
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.2142857142857143e-06,
      "loss": 2.441,
      "step": 1314
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.178571428571429e-06,
      "loss": 2.1993,
      "step": 1315
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.1428571428571433e-06,
      "loss": 2.4635,
      "step": 1316
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.1071428571428574e-06,
      "loss": 2.1616,
      "step": 1317
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.0714285714285715e-06,
      "loss": 2.1853,
      "step": 1318
    },
    {
      "epoch": 1.88,
      "learning_rate": 3.035714285714286e-06,
      "loss": 1.9946,
      "step": 1319
    },
    {
      "epoch": 1.89,
      "learning_rate": 3e-06,
      "loss": 2.4408,
      "step": 1320
    },
    {
      "epoch": 1.89,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.246150255203247,
      "eval_runtime": 75.5597,
      "eval_samples_per_second": 3.084,
      "eval_steps_per_second": 1.548,
      "step": 1320
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.9642857142857146e-06,
      "loss": 2.0293,
      "step": 1321
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.9285714285714287e-06,
      "loss": 2.2102,
      "step": 1322
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.892857142857143e-06,
      "loss": 2.4422,
      "step": 1323
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.8571428571428573e-06,
      "loss": 2.3465,
      "step": 1324
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.8214285714285713e-06,
      "loss": 2.2212,
      "step": 1325
    },
    {
      "epoch": 1.89,
      "learning_rate": 2.785714285714286e-06,
      "loss": 2.5418,
      "step": 1326
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.7500000000000004e-06,
      "loss": 2.4121,
      "step": 1327
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.7142857142857144e-06,
      "loss": 2.5173,
      "step": 1328
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.6785714285714285e-06,
      "loss": 2.2216,
      "step": 1329
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.642857142857143e-06,
      "loss": 2.1614,
      "step": 1330
    },
    {
      "epoch": 1.9,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2433810234069824,
      "eval_runtime": 75.4311,
      "eval_samples_per_second": 3.089,
      "eval_steps_per_second": 1.551,
      "step": 1330
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.607142857142857e-06,
      "loss": 2.2396,
      "step": 1331
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.5714285714285716e-06,
      "loss": 2.5028,
      "step": 1332
    },
    {
      "epoch": 1.9,
      "learning_rate": 2.5357142857142857e-06,
      "loss": 2.676,
      "step": 1333
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.5e-06,
      "loss": 2.6356,
      "step": 1334
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.4642857142857143e-06,
      "loss": 2.6346,
      "step": 1335
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.428571428571429e-06,
      "loss": 2.5284,
      "step": 1336
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.392857142857143e-06,
      "loss": 2.1991,
      "step": 1337
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.3571428571428574e-06,
      "loss": 2.1583,
      "step": 1338
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.3214285714285715e-06,
      "loss": 2.169,
      "step": 1339
    },
    {
      "epoch": 1.91,
      "learning_rate": 2.285714285714286e-06,
      "loss": 2.3998,
      "step": 1340
    },
    {
      "epoch": 1.91,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2404403686523438,
      "eval_runtime": 72.1214,
      "eval_samples_per_second": 3.231,
      "eval_steps_per_second": 1.622,
      "step": 1340
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.25e-06,
      "loss": 2.0472,
      "step": 1341
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.214285714285714e-06,
      "loss": 2.2231,
      "step": 1342
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.1785714285714286e-06,
      "loss": 2.267,
      "step": 1343
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.142857142857143e-06,
      "loss": 2.3332,
      "step": 1344
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.1071428571428572e-06,
      "loss": 2.0497,
      "step": 1345
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.0714285714285713e-06,
      "loss": 2.2849,
      "step": 1346
    },
    {
      "epoch": 1.92,
      "learning_rate": 2.035714285714286e-06,
      "loss": 2.0941,
      "step": 1347
    },
    {
      "epoch": 1.93,
      "learning_rate": 2.0000000000000003e-06,
      "loss": 1.8435,
      "step": 1348
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.9642857142857144e-06,
      "loss": 2.4522,
      "step": 1349
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.9285714285714285e-06,
      "loss": 2.18,
      "step": 1350
    },
    {
      "epoch": 1.93,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2396936416625977,
      "eval_runtime": 77.0807,
      "eval_samples_per_second": 3.023,
      "eval_steps_per_second": 1.518,
      "step": 1350
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.892857142857143e-06,
      "loss": 2.043,
      "step": 1351
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.8571428571428573e-06,
      "loss": 2.3128,
      "step": 1352
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.8214285714285716e-06,
      "loss": 2.0442,
      "step": 1353
    },
    {
      "epoch": 1.93,
      "learning_rate": 1.7857142857142857e-06,
      "loss": 2.2448,
      "step": 1354
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.7500000000000002e-06,
      "loss": 2.311,
      "step": 1355
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.7142857142857145e-06,
      "loss": 2.3645,
      "step": 1356
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.6785714285714286e-06,
      "loss": 2.5319,
      "step": 1357
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.6428571428571429e-06,
      "loss": 2.3242,
      "step": 1358
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.6071428571428572e-06,
      "loss": 2.0698,
      "step": 1359
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.5714285714285717e-06,
      "loss": 2.5383,
      "step": 1360
    },
    {
      "epoch": 1.94,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2369773387908936,
      "eval_runtime": 74.7829,
      "eval_samples_per_second": 3.116,
      "eval_steps_per_second": 1.565,
      "step": 1360
    },
    {
      "epoch": 1.94,
      "learning_rate": 1.5357142857142857e-06,
      "loss": 2.1647,
      "step": 1361
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.5e-06,
      "loss": 2.3315,
      "step": 1362
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.4642857142857143e-06,
      "loss": 2.3433,
      "step": 1363
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.4285714285714286e-06,
      "loss": 2.5682,
      "step": 1364
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.392857142857143e-06,
      "loss": 2.0621,
      "step": 1365
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.3571428571428572e-06,
      "loss": 2.3018,
      "step": 1366
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.3214285714285715e-06,
      "loss": 2.1397,
      "step": 1367
    },
    {
      "epoch": 1.95,
      "learning_rate": 1.2857142857142858e-06,
      "loss": 2.3151,
      "step": 1368
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.25e-06,
      "loss": 2.3104,
      "step": 1369
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.2142857142857144e-06,
      "loss": 2.6089,
      "step": 1370
    },
    {
      "epoch": 1.96,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2358577251434326,
      "eval_runtime": 72.6189,
      "eval_samples_per_second": 3.209,
      "eval_steps_per_second": 1.611,
      "step": 1370
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.1785714285714287e-06,
      "loss": 1.9291,
      "step": 1371
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.142857142857143e-06,
      "loss": 2.0656,
      "step": 1372
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.107142857142857e-06,
      "loss": 2.4072,
      "step": 1373
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.0714285714285716e-06,
      "loss": 2.5933,
      "step": 1374
    },
    {
      "epoch": 1.96,
      "learning_rate": 1.0357142857142857e-06,
      "loss": 2.1318,
      "step": 1375
    },
    {
      "epoch": 1.97,
      "learning_rate": 1.0000000000000002e-06,
      "loss": 2.446,
      "step": 1376
    },
    {
      "epoch": 1.97,
      "learning_rate": 9.642857142857142e-07,
      "loss": 2.3725,
      "step": 1377
    },
    {
      "epoch": 1.97,
      "learning_rate": 9.285714285714287e-07,
      "loss": 2.2971,
      "step": 1378
    },
    {
      "epoch": 1.97,
      "learning_rate": 8.928571428571428e-07,
      "loss": 2.4436,
      "step": 1379
    },
    {
      "epoch": 1.97,
      "learning_rate": 8.571428571428572e-07,
      "loss": 2.4884,
      "step": 1380
    },
    {
      "epoch": 1.97,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.2360756397247314,
      "eval_runtime": 72.6984,
      "eval_samples_per_second": 3.205,
      "eval_steps_per_second": 1.609,
      "step": 1380
    },
    {
      "epoch": 1.97,
      "learning_rate": 8.214285714285714e-07,
      "loss": 2.2088,
      "step": 1381
    },
    {
      "epoch": 1.97,
      "learning_rate": 7.857142857142858e-07,
      "loss": 2.1817,
      "step": 1382
    },
    {
      "epoch": 1.98,
      "learning_rate": 7.5e-07,
      "loss": 2.3101,
      "step": 1383
    },
    {
      "epoch": 1.98,
      "learning_rate": 7.142857142857143e-07,
      "loss": 2.3833,
      "step": 1384
    },
    {
      "epoch": 1.98,
      "learning_rate": 6.785714285714286e-07,
      "loss": 2.4587,
      "step": 1385
    },
    {
      "epoch": 1.98,
      "learning_rate": 6.428571428571429e-07,
      "loss": 2.2791,
      "step": 1386
    },
    {
      "epoch": 1.98,
      "learning_rate": 6.071428571428572e-07,
      "loss": 2.0987,
      "step": 1387
    },
    {
      "epoch": 1.98,
      "learning_rate": 5.714285714285715e-07,
      "loss": 2.1659,
      "step": 1388
    },
    {
      "epoch": 1.98,
      "learning_rate": 5.357142857142858e-07,
      "loss": 2.1215,
      "step": 1389
    },
    {
      "epoch": 1.99,
      "learning_rate": 5.000000000000001e-07,
      "loss": 2.378,
      "step": 1390
    },
    {
      "epoch": 1.99,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.236154079437256,
      "eval_runtime": 75.1127,
      "eval_samples_per_second": 3.102,
      "eval_steps_per_second": 1.558,
      "step": 1390
    },
    {
      "epoch": 1.99,
      "learning_rate": 4.642857142857143e-07,
      "loss": 2.3594,
      "step": 1391
    },
    {
      "epoch": 1.99,
      "learning_rate": 4.285714285714286e-07,
      "loss": 2.2443,
      "step": 1392
    },
    {
      "epoch": 1.99,
      "learning_rate": 3.928571428571429e-07,
      "loss": 2.417,
      "step": 1393
    },
    {
      "epoch": 1.99,
      "learning_rate": 3.5714285714285716e-07,
      "loss": 2.0812,
      "step": 1394
    },
    {
      "epoch": 1.99,
      "learning_rate": 3.2142857142857145e-07,
      "loss": 2.3694,
      "step": 1395
    },
    {
      "epoch": 1.99,
      "learning_rate": 2.8571428571428575e-07,
      "loss": 2.308,
      "step": 1396
    },
    {
      "epoch": 2.0,
      "learning_rate": 2.5000000000000004e-07,
      "loss": 2.2354,
      "step": 1397
    },
    {
      "epoch": 2.0,
      "learning_rate": 2.142857142857143e-07,
      "loss": 2.3666,
      "step": 1398
    },
    {
      "epoch": 2.0,
      "learning_rate": 1.7857142857142858e-07,
      "loss": 2.1337,
      "step": 1399
    },
    {
      "epoch": 2.0,
      "learning_rate": 1.4285714285714287e-07,
      "loss": 2.438,
      "step": 1400
    },
    {
      "epoch": 2.0,
      "eval_cer": 0.9743164321741439,
      "eval_loss": 2.235908031463623,
      "eval_runtime": 81.662,
      "eval_samples_per_second": 2.853,
      "eval_steps_per_second": 1.433,
      "step": 1400
    }
  ],
  "max_steps": 1400,
  "num_train_epochs": 2,
  "total_flos": 1.4920051102580736e+18,
  "trial_name": null,
  "trial_params": null
}

'''

# Load the JSON data
data = json.loads(json_data)

# Extract the loss values, handling missing 'loss' key
loss_values = []
for entry in data["log_history"]:
    if "loss" in entry:
        loss_values.append(entry["loss"])
    else:
        print("Entry missing 'loss' key:", entry)

# Create the plot if there are loss values
if loss_values:
    plt.figure(figsize=(10, 6))
    plt.plot(loss_values)
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.title('Training error')
    plt.grid(True)

    # Save the plot as an image file (e.g., PNG)
    plt.savefig('loss_plot.png')

    # Display a message indicating successful save
    print("Plot saved as loss_plot.png")
else:
    print("No loss values found. Cannot create the plot.")