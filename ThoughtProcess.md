# Why I designed this the way I did
The original Twitter example was essentially showing students how to
use a Python wrapper for a Web API. From my interview with Lisa
it seemed that Corporate customers find Twitter to be a toy example
and not practical. I also got feedback that the customers were
likely in the financial sector.  

Due to this I chose to use the Quandl api for numerous 
reasons. One is that professionals taking this course
will likely have experience with the stock market so this should
feel more relevant and useful.  
  
The second was that Quandl also published a Python API wrapper in top
of its http interface. Students should be familiar with pandas dataframes,
loops, and imports at this point in their education and I found that this
particular library fit those constraints. I also found that the documentation
was quite good, which also serves as a learning exercise for students
that reading documentation is the best way to implement code, especially
without if a instructor/mentor is not present.
  
Lastly I chose Quandl because we already use it in the Front End section
of the course, making it easier for curriculum engineers to
maintain curriculum due to consistency. It also means that if the
corporate customer wants a Front End lecture the students
will already be familiar with the api.
