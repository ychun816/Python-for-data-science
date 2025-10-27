
| Function / Method / Operation                          | Library              | Usage / Purpose                                | Example / Notes                                        |
| ------------------------------------------------------ | -------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| `os.path.dirname(__file__)`                            | os                   | Returns the directory path of the current file | Useful for building relative paths                     |
| `os.path.join(a, b)`                                   | os                   | Joins paths in a platform-independent way      | `'folder' + 'file.csv'` → `'folder/file.csv'` on Linux |
| `load(path)`                                           | custom               | Loads a CSV into a Pandas DataFrame            | Returns a DataFrame with CSV content                   |
| `df['country'].values`                                 | pandas               | Access the underlying numpy array of a column  | Use to check if a value exists with `in`               |
| `df[df['country'] == country]`                         | pandas               | Filters rows where column matches a value      | Returns a new DataFrame with only matching rows        |
| `.drop(columns='country')`                             | pandas               | Remove one or more columns from DataFrame      | Useful to focus only on numeric columns for plotting   |
| `.T`                                                   | pandas               | Transpose a DataFrame (swap rows and columns)  | Converts single row into column with index as years    |
| `.columns = ['Life Expectancy']`                       | pandas               | Rename column(s)                               | Makes plot easier to understand                        |
| `.index.name = 'Year'`                                 | pandas               | Give the index a name                          | Helps when resetting index for plotting                |
| `.reset_index(inplace=True)`                           | pandas               | Converts index into a normal column            | Needed for Seaborn plotting with columns as x/y        |
| `.astype(int)` / `.astype(float)`                      | pandas               | Convert data types                             | Ensures numeric types for plotting                     |
| `sns.set_theme()`                                      | seaborn              | Set a default theme for plots                  | Changes style (background, colors) globally            |
| `sns.lineplot(data=df, x='Year', y='Life Expectancy')` | seaborn              | Create a line chart                            | Returns an Axes object to customize further            |
| `.set_title('title')`                                  | matplotlib / seaborn | Set the plot’s title                           | Can also adjust fontsize, fontweight                   |
| `plticker.MultipleLocator(base=40)`                    | matplotlib.ticker    | Create ticks at fixed intervals                | base=40 → every 40 years                               |
| `ax.xaxis.set_major_locator(locator)`                  | matplotlib           | Apply tick locator to x-axis                   | Control how often ticks appear                         |
| `plt.show()`                                           | matplotlib.pyplot    | Display the figure                             | Blocks execution until window is closed                |
| `try … except Exception as e`                          | Python built-in      | Handle errors safely                           | Useful to catch any runtime error                      |
| `raise RuntimeError(f"...")`                           | Python built-in      | Re-throw an error with custom message          | Keeps program robust and debuggable                    |
              |

---

### 🔹 Key Notes for Learning

1. **Pandas**:

   * `df[column]` → select a column
   * `df[condition]` → filter rows
   * `.drop()`, `.T`, `.reset_index()`, `.astype()` → data cleaning & reshaping

2. **Seaborn + Matplotlib**:

   * `sns.lineplot()` → quick plotting
   * Axes object (`ax`) → customize titles, labels, and ticks
   * `plt.show()` → finally display plot

3. **Python basics**:

   * `try/except` → handle exceptions
   * `raise` → propagate errors
   * `os.path` → manage file paths safely

