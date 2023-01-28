##  MongoDB Exercise :  Questions
1. Write a MongoDB query to display all the documents in the collection restaurants.

2. Write a MongoDB query to display the fields restaurant_id, name, borough, and cuisine for all the documents in the collection restaurant.

3. Write a MongoDB query to display the fields restaurant_id, name, borough, and cuisine, but exclude the field _id_ for all the documents in the collection restaurant.

4. Write a MongoDB query to display the fields zip code, but exclude the field _id_ for all the documents in the collection restaurant.

5. Write a MongoDB query to display all the restaurants which are in the borough Brooklyn.

6. Write a MongoDB query to display the first 5 restaurants which are in the borough Brooklyn.

7. Write a MongoDB query to display the next 5 restaurants after skipping the first 5 which are in the borough Brooklyn.

8. Write a MongoDB query to find the restaurants that achieved a score of more than 7.

9. Write a MongoDB query to find the restaurants that achieved a score, of more than 7 but less than 10.

10. Write a MongoDB query to find the restaurants that do not prepare any cuisine of ‘American’ and their grade score of more than 7.

11. Write a MongoDB query to find the restaurants which do not prepare any cuisine of ‘American’ and achieved a grade point ‘A’ not belonging to the borough Brooklyn. The document must be displayed according to the cuisine in descending order.

12. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which contain ‘Wil’ as the first three letters of their name.

13. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which contain ‘Food’ as the last three letters of their name.

14. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which contain ‘Seafood’ as three letters somewhere in their name.

15. Write a MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dishes.

16. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which belong to the borough of Staten Island or Queens, or Bronx Brooklyn.

17. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which do not belong to the borough Staten Island or Queens, or Bronxor Brooklyn.

18. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which achieved a score that is not more than 10.

19. Write a MongoDB query to find the restaurant Id, name, borough, and cuisine for those restaurants which prepared dishes except ‘American’ and ‘Chinese’ or the restaurant’s name begins with the letter ‘Sea’.

20. Write a MongoDB query to arrange the name of the restaurants in ascending order along with all the columns.

21. Write a MongoDB query to arrange the name of the restaurants in descending order along with all the columns.

22. Write a MongoDB query to arrange the name of the cuisine in ascending order and for that same cuisine, the borough should be in descending order.

23. Write a MongoDB query to know whether all the addresses contain the building or not.

24. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants where the 2nd element of the grades array contains a grade of “A” and score 9 on an ISODate “2013–09–11T00:00:00Z”.

25. Write a MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of “A” and scored 11 on an ISODate “2013–09–11T00:00:00Z” among many of the survey dates.

26. Write a MongoDB query that will select all documents in the restaurants' collection where the coord field value is double.

27. Write a MongoDB query that will select the restaurant Id, name, and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.

28. Write a query to find the restaurants with more than three grade surveys (‘grades’ Array contains more than three elements) and display only the name and the number of grades.

29. Write an aggregation pipeline to count the number of restaurants in the borough “Bronx” for each cuisine type. Display the number of restaurants that prepare Caribbean cuisine. A single query is expected that satisfies all the above requirements.
