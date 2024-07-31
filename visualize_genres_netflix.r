install.packages("ggplot2")

library(readr)
genres_data <- read_csv("C:/Users/DELL/Downloads/most_common_genres.csv")

library(ggplot2)
ggplot(genres_data, aes(x = reorder(genre, count), y = count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +
  labs(title = "Most Common Genres",
       x = "Genre",
       y = "Count") +
  theme_minimal()

ggsave("most_common_genres_plot.png")
