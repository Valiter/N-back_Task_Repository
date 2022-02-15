

def analyzer_n_back(stymulus_line, stimulus_index, interval_to_back):
    if stimulus_index >= interval_to_back + 1:
        index_minus_interval = stimulus_index + 1
        if stymulus_line[index_minus_interval] == stymulus_line[stimulus_index]:
            return True
    return False

