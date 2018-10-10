import numpy as np 
import fetchmaker_1
from scipy.stats import binom_test
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker_1.get_tail_length("rottweiler")

print (np.mean(rottweiler_tl))
print (np.std(rottweiler_tl))

whippet_rescue = fetchmaker_1.get_is_rescue("whippet")

num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

whippets_rescue_pvalue = binom_test(num_whippet_rescues, num_whippets, p = .08)
print (whippets_rescue_pvalue)

whippet_weights = fetchmaker_1.get_weight("whippet")
terrier_weights = fetchmaker_1.get_weight("terrier")
pitbull_weights = fetchmaker_1.get_weight("pitbull")

#anova comparing whippet, terrier, and pitbull weights
whippet_terrier_pitbull_anova = f_oneway(whippet_weights, terrier_weights, pitbull_weights)
print (whippet_terrier_pitbull_anova)

#combining the smaller weight lists and making a list of labels to use the tukey test
whippets_terriers_pitbulls = np.concatenate([whippet_weights, terrier_weights, pitbull_weights])
labels = ["whippet"] * len(whippet_weights) + ["terrier"] * len(terrier_weights) + ["pitbull"] * len(pitbull_weights)

tukey_results = pairwise_tukeyhsd(whippets_terriers_pitbulls, labels, .05)

poodle_colors = fetchmaker_1.get_color("poodle")
shihtzu_colors = fetchmaker_1.get_color("shihtzu")

color_table = [
	[np.count_nonzero(poodle_colors == "black" ), np.count_nonzero(shihtzu_colors == "black")],
	[np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")],
	[np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")],
	[np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")],
	[np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]

chi2, pval, dof, expfreq = chi2_contingency(color_table)
print (pval) 