
import pandas as pd

#Load our dataset
data = pd.read_csv("C:/Users/Admin/PycharmProjects/student-performance-analysis/data/StudentsPerformance.csv")
#display the first five students

print(data.head())

print("Dataset shape:")
print(data.shape)

print("Column names:")
print(data.columns.tolist())

print("Statistical summary:")
print(data[["math score", "reading score", "writing score"]].describe())

# Select the three exam score columns
scores = data[["math score", "reading score", "writing score"]]

# Calculate descriptive statistics
print("\nDESCRIPTIVE STATISTICS")
print("Mean:")
print(scores.mean())

print("\nMedian:")
print(scores.median())

print("\nMode:")
print(scores.mode().iloc[0])

print("\nRange:")
print(scores.max() - scores.min())

print("\nStandard deviation:")
print(scores.std())

import matplotlib.pyplot as pit

#select mathematics scores
math_scores =data["math score"]

#create a histogram
pit.hist(math_scores,bins=10,edgecolor="black")

#add labels and titles
pit.title("Distribution of Mathematics scores")
pit.xlabel("Mathematics score")
pit.ylabel("Number of students")

#Display the graph
pit.tight_layout()
pit.show()

#calculate average scores
subjects=["math score", "reading score", "writing score"]
average_scores=data[subjects].mean()

#create a bar chat
pit.bar(
    ["Mathematics","reading score","writing score"],
    average_scores.values,
    edgecolor="black",
     )

#add titles and labels
pit.title("Average student scores by subject")
pit.xlabel("Subjects")
pit.ylabel("Average score")

#keeping the layout neat
pit.tight_layout()

#Displaying the graph
pit.show()

#calculating average scores
average_scores =data[["math score", "reading score", "writing score"]].mean()

#calculate the difference
writing_math_difference =(
    average_scores["writing score"]
    - average_scores["math score"]

)

print("\n COMPARISON OF WRITING AND MATHEMATICS")
print(f"Average writing score :{average_scores['writing score']}")
print(f"Mathematics score:{average_scores['math score']}")
print("Difference",writing_math_difference)

#Round scores to 2 decimal places
math_average =round(data["math score"].mean(),2)
wring_average=round(data["writing score"].mean(),2)

difference=round(writing_math_difference,2)

print("\n STATISTICAL FINDINGS")
print("--------------------------------------")
print(f"Average mathematics score ;{math_average}")
print(f"Average writing score ;{wring_average}")
print(f"Difference ;{difference} points")


df =pd.read_csv("C:/Users/Admin/PycharmProjects/student-performance-analysis/data/StudentsPerformance.csv")

math_std=df["math score"].std()
reading_std=df["reading score"].std()
writing_std=df["writing score"].std()

print("\n")
print("Mathematics standard deviation",math_std)
print("Reading standard deviation",reading_std)
print("Writing standard deviation",writing_std)


print("\n")
#store the standard deviations
subjects=["mathematics", "Reading", "Writing"]

standard_deviations=[math_std,
                     reading_std,
                     writing_std
                     ]

print(subjects)
print(standard_deviations)

#create a bar chart
pit.figure(figsize=(8,5))

bars=pit.bar(subjects,standard_deviations)

#Add a title and labels
pit.title("Standard deviation of Student Scores by Subject ")
pit.xlabel("Subject")
pit.ylabel("Standard deviation")

#Display the value above each bar
pit.bar_label(bars,fmt="%.2f",padding=3)

# Improve the layout
pit.tight_layout()

# Save the graph as an image
pit.savefig("images/standard_deviation_comparison.png", dpi=300, bbox_inches="tight")
# Display the graph
pit.show()


#compare average scores by subject

math_mean = df["math score"].mean()
reading_mean = df["reading score"].mean()
writing_mean = df["writing score"].mean()


#calculating the difference btn average reading and average scores

reading_math_difference = reading_mean-math_mean

print("\n")
print("Difference between reading and math average :",
     round(reading_math_difference,2))


subjects=["Mathematics", "Reading", "Writing "]
average_scores=[math_mean,reading_mean,writing_mean]

#Find the highest and the lowest average scores

highest_average=max(average_scores)
lowest_average=min(average_scores)

#identifying the subjects with thw highest and lowest  averages

highest_index= average_scores.index(highest_average)
lowest_index= average_scores.index(lowest_average)

highest_subject = subjects[highest_index]
lowest_subject = subjects[lowest_index]

print("\n")
print("Subject with th highest average:",highest_subject)
print("Subject with lowest average:",lowest_subject)

score_gap=highest_average-lowest_average


print("\n---------Statistical summary---------------")
print(f"{highest_subject} had the highest average score"
      f"of {highest_average:.2f}"
      )
print(f"{lowest_subject} had the lowest average score"
      f"of {lowest_average:.2f}"
      )

print(f"The difference  between the highest and lowest "
      f"averages was {score_gap:.2f} points"
      )

print("\n")
print ("Highest average:",highest_average)
print ("Lowest average:",lowest_average)
print("Gap between highest average and lowest average:",round(score_gap,2))


print("\n")
print("Mathematics mean",math_mean)
print("Reading mean",reading_mean)
print("Writing mean",writing_mean)
print("average_scores",average_scores)


pit.figure(figsize=(8,5))
bars=pit.bar(subjects,average_scores)

pit.title("Average Student Scores by Subject ")
pit.xlabel("Subject")
pit.ylabel("Average score")

pit.bar_label(bars,fmt="%.2f",padding=3)


pit.tight_layout()
pit.savefig("images/average_scores_comparison.png", dpi=300, bbox_inches="tight")
pit.show()







