## What
___

Added a pipelines to compute statistics for our data. The pipeline calculates the Gini Coefficient, H-Index, and 
Simpson's evenness.

## Why
___

The `scipy.stats` module has a bug that probably won't get fixed for a while and we need to get our results soon.

## How
___

I followed the formulas from [statisticshowto](https://www.statisticshowto.com/simpsons-diversity-index/) and
implemented this into a single pipeline

### Changes details
* Added `h_index()` function to compute Shannon's H
* Added `gini_coefficient()` function to compute the Gini Coefficient
* Added `simpsons_evenness()` function to compute Simpson's E
* Added `stats_pipeline()` function to run these all at one time for each dataset we pass to it

## Missed anything?
___
- [ ] Explained the purpose of this PR
- [ ] Self reviewed this PR
- [ ] Added or updated test cases
- [ ] Updated documentation (if applicable)
- [ ] Added screenshots (if applicable)


Reference for this template: [Tomek Kolasa](https://tomekkolasa.com/how-to-make-great-pull-requests)
