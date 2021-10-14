# Surf's Up - Surf and Shake Shop

## Objective
The owner of Vemtures, Inc. ("VI") recently visited Hawaii and based on his observations and desire to live permantly in the area, he has developed an idea for a Surf and Shake Shop - a shop on the beach of Oahu which would sell and rent surf boards to surfers while also offering fresh-made shakes to all customers visiting the area.  VI is excited about this new venture and seeks investment capital from W. Avy, a well-known investor an surfing afficionado.  W. Avy is very entusiastic about VI's venture, but has some concerns about ensuring the weather pattern in the area is optimal and supports a shop of this nature over the long haul.  The last venture he invested in like this was a failure due to consistently bad weather where the shop was located.  W. Avy has asked for descriptive analytics of weather data for the beach of Oahu, Hawaii.

To fulfill W. Avy's request, VI will use Python, Pandas functions and methods, and SQLAlchemy to filter data from weather data collected from various weather stations in the area for the  years 2010 to 2017.  VI will look at temperatures for these years, specifically in the months of June to reprsent summer months and December to represent winter months.

## Results
The results of this analysis proved the weather temperatures to comfortable for tourits and stable enough over the two periods to encourage a healthy and consistent tourist visitation.   

Analysis for temperatures in June timefram for years 2010 to 2017 are:

![June_temps](https://user-images.githubusercontent.com/35401581/137364423-664f599f-b592-44ed-9dda-1d3161071911.png)


Analysis for temperatures in December timefram for years 2010 to 2017 are:

![Dec_temps](https://user-images.githubusercontent.com/35401581/137364426-27c076c2-5ed2-4eea-b72e-a9ad5cb36f96.png)

* The range of temperatures (farenheit) proved surprisingly but reassuringly consistent between the two periods of time (i.e. June for typically warmer months and December for typically cooler months).  The June range of temperatures was a min of 64 degrees and a max of 85 degrees.  The December range of temperatures was a min of 56 degrees just 8 degrees cooler at times and a max of 83 degrees closely matching June's temperature max at 85 degrees.
* Further support for temperatures being consistent between June and December is the average temperatures being within 4 degrees of each other:  75 degrees for June and 71 degrees for December.
* The percentile averages also support a consistent and comforable visitng weather pattern over the 2 periods:
    * June percentile temperatures are: 25%tile is 73, 50%tile is 75, and 75%tile is 77
    * December percentile temperatures are: 25%tile is 69, 50%tile is 71, and 75%tile is 74   

## Summary
So far, this data supports VI's Surf and Shake Shop venture initiative.  However, it would only be right to look at precipitation data over these time periods as well for a final confirmation that potential visitors will experience fair and comfortable weather most of the time.  For this purpose VI has also run the following precipation data:

*  VI queried precipation data over the years 2010 through 2017 for the month of June along with statistics for averages and percentiles.
*  VI queried precipation data over the years 2010 through 2017 for the month of December along with statistics for averages and percentiles.

Once again, this data ensures 75 percent of the time rainfall precipitation will be minimal, with the 75%tile data showing 0.12 inches for June months and 0.15 inches for December months.

 
