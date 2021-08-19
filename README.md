# Big_Data_Map_Reduce

The aim of this project was to use Hadoop Map Reduce framework to find the descriptive statistics of weather throughout weather stations April 2007. Thisss repossitory contains; the mapper and reduce scripts, the output for each task, and the overall report.   

MapReduce almost acts like a divide and conquer algorithm, by breaking down the problem into two or more subproblems/tasks. The map function takes a key-value pair as an input and outputs a key-value pair, whilst only making one map call for every key-value pair (Dean and Ghemawat, 2004; Leskovec, Rajaraman and Ullman, 2014). The second step is not programmed by the user and results in grouping the same keys together and ordering them. This step is considered the shuffling of the Map tasks output – the key-value pairs. These pairs are then fed into the reduce function as an input. All the values with the same key are reduced together and there is one reduce function call per unique key (Dean and Ghemawat, 2004). Typically, during this step some sort of computation occurs to the values in the key-value groups. For the purpose of this project, this step involved calculating; the daily min and max dry bulb temperatures, the daily average dry bulb temperature, and daily standard deviation of the dry bulb temperature. 


<b>References</b>

Dean, J. and Ghemawat, S., 2004. MapReduce: Simplified data processing on large clusters.[online] Available at: https://static.usenix.org/publications/library/proceedings/osdi04/tech/full_papers/dean/dean.pdf [Accessed 21 June 2021].

Leskovec, J., Rajaraman, A. and Ullman, J., 2014. 3rd ed. Cambridge: Cambridge University Press, pp.25-31. [online] Available at: http://infolab.stanford.edu/~ullman/mmds/ch2.pdf [Accessed 21 June 2021].

