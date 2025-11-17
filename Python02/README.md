# Python02 | DataTable

[Back to Index](../README.md)
---

## ex01 
life_expectancy function syntax: 

🔹 Key Notes for Learning: 
1. Pandas:
- `df[column]` → select a column
- `df[condition]` → filter rows
- `.drop()`, `.T`, `.reset_index()`, `.astype()` → data cleaning & reshaping
2. Seaborn + Matplotlib:
- `sns.lineplot()` → quick plotting
- `Axes object (ax)` → customize titles, labels, and ticks
- `plt.show()` → finally display plot
3. Python basics:
- `try/except` → handle exceptions
- `raise` → propagate errors
- `os.path` → manage file paths safely



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


How CSV goes from raw file → Pandas DataFrame → cleaned / transposed → plotted with Seaborn/Matplotlib.

```yaml
CSV File (life_expectancy_years.csv)
┌─────────┬──────┬──────┬──────┐
│ country │ 1800 │ 1801 │ 1802 │ ...
├─────────┼──────┼──────┼──────┤
│ France  │ 43.5 │ 44.2 │ 44.8 │ ...
│ Spain   │ 35.2 │ 35.9 │ 36.5 │ ...
└─────────┴──────┴──────┴──────┘
        |
        | load(path)  ← your custom function
        v
Pandas DataFrame (raw)
df = load(path)
┌─────────┬──────┬──────┬──────┐
│ country │ 1800 │ 1801 │ 1802 │ ...
├─────────┼──────┼──────┼──────┤
│ France  │ 43.5 │ 44.2 │ 44.8 │ ...
└─────────┴──────┴──────┴──────┘
        |
        | Filter row by country: df[df['country'] == country]
        v
Filtered row
┌─────────┬──────┬──────┬──────┐
│ country │ 1800 │ 1801 │ 1802 │ ...
├─────────┼──────┼──────┼──────┤
│ France  │ 43.5 │ 44.2 │ 44.8 │ ...
└─────────┴──────┴──────┴──────┘
        |
        | Drop 'country' column: .drop(columns='country')
        v
Numeric data only
┌──────┬──────┬──────┐
│ 1800 │ 1801 │ 1802 │ ...
├──────┼──────┼──────┤
│ 43.5 │ 44.2 │ 44.8 │ ...
└──────┴──────┴──────┘
        |
        | Transpose: .T
        v
Transposed DataFrame
┌──────┬─────────────────┐
│Year  │ Life Expectancy │
├──────┼─────────────────┤
│ 1800 │ 43.5            │
│ 1801 │ 44.2            │
│ 1802 │ 44.8            │
└──────┴─────────────────┘
        |
        | Reset index: .reset_index(inplace=True)
        | Convert types: .astype(int/float)
        v
Cleaned DataFrame (ready for plotting)
┌──────┬─────────────────┐
│Year  │ Life Expectancy │
├──────┼─────────────────┤
│ 1800 │ 43.5            │
│ 1801 │ 44.2            │
│ 1802 │ 44.8            │
└──────┴─────────────────┘
        |
        | Plot: sns.lineplot(data=df, x='Year', y='Life Expectancy')
        | Customize: ax.set_title(), ax.xaxis.set_major_locator()
        v
Line Plot (Seaborn/Matplotlib)
```

### Concept Made Clearer

####  🧩 `from typing import Optional` ?

`typing` is a **standard Python module** used for **type hints** — hints that help you (and tools like IDEs or linters) understand what kind of data a variable or function expects.

`Optional[T]` means:

> The variable can either be of type **T** or **None**.

##### Example:

```python
from typing import Optional

def greet(name: Optional[str]) -> None:
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")
```

Here:

* `name` can be a string (`"Alice"`)
* or `None` (meaning no name provided)

So both of these are valid:

```python
greet("Alice")   # ✅ prints "Hello, Alice!"
greet(None)      # ✅ prints "Hello, stranger!"
```

In your code:

```python
def life_expectancy(
    country: str,
    save_path: Optional[str] = None,
    ...
)
```

→ means `save_path` might be a string (like `"plot.png"`) **or** `None` (meaning: don’t save to file — show the plot on screen instead).

---

#### 🧩  Why need `_import_ex00_loader()` ?

Normally, we’d just import a function like this:

```python
from ex00.load_csv import load
```

But here’s the problem:

* The loader file (`ex00/load_csv.py`) may **not exist yet**, depending on how the project is structured.
* Importing it directly at the **top level** would cause **file I/O or ImportError** immediately when the module loads — even if you’re not calling it yet.

That’s risky because:

* Imports should be lightweight (no heavy disk access or computation).
* You only want to run I/O **when you actually call** the function.

So the author built `_import_ex00_loader()` to **delay** importing the `load()` function until runtime — when it’s really needed.

---

##### 🔁 What happens visually (ASCII Diagram)

```
+----------------------------------------------------------+
| main script (life_expectancy.py)                         |
|                                                          |
|   when Python imports this file:                         |
|     - NO CSV is loaded yet                               |
|     - NO file is opened                                  |
|                                                          |
|   later, when life_expectancy() runs:                    |
|                                                          |
|   ┌────────────────────────────┐                         |
|   │ calls _import_ex00_loader()│                         |
|   └──────────────┬─────────────┘                         |
|                  │                                       |
|                  ▼                                       |
|        _import_ex00_loader() function                    |
|        checks:                                           |
|          • Is ex00/load_csv.py file present?             |
|            → Yes → load it dynamically using importlib   |
|          • If not, try local load_csv.py instead         |
|                                                          |
|   returns: load function handle (module.load)            |
|                                                          |
|   life_expectancy() then calls:                          |
|       data = loader("life_expectancy_years.csv")         |
|                                                          |
+----------------------------------------------------------+
```

👉 This ensures that **no heavy code runs until you actually call** `life_expectancy()`.

---

#### 🧱 DatasetView and `.raw()` method

Now, this part refers to how data is *wrapped* or *encapsulated* by another object.

##### Step-by-step idea:

* The `ex00/load_csv.py` loader doesn’t return a plain pandas DataFrame.
* Instead, it returns a special object called `DatasetView`, which is a *wrapper* around a DataFrame.

So you have this situation:

```
┌────────────────────────────-─┐
│ DatasetView object           │
│ ───────────────────────────  │
│ contains:                    │
│   self._df = pandas.DataFrame│
│                              │
│ and methods:                 │
│   .raw() → returns self._df  │
│   .__repr__() → preview text │
└───────────────────────────-──┘
```

This lets you **print** a short preview instead of a huge table:

```python
v = load("data.csv")
print(v)
# Loading dataset of dimensions (200, 10)
# country year ... population
# France 1950 ... 42.5
```

But if you actually want to work with the raw pandas data:

```python
df = v.raw()
print(df.head())  # Full DataFrame
```

---

#### 🧩 So this check makes sense:

```python
if hasattr(data, 'raw'):
    df = data.raw()  # unwrap to get real DataFrame
else:
    df = data        # if it's already a DataFrame, use it
```

#### 🧠 ASCII Visualization:

```
Case 1: Loader returns DatasetView
----------------------------------
data ──▶ DatasetView
          └──▶ _df (pandas.DataFrame)
                ↑
                └── accessed by .raw()


Case 2: Loader returns DataFrame directly
-----------------------------------------
data ──▶ pandas.DataFrame  (no wrapper, no .raw() needed)
```

So your code safely handles **both cases** without error.

---

#### 🧭 Summary

| Concept                  | Meaning                                         | Why it’s used                                      |
| ------------------------ | ----------------------------------------------- | -------------------------------------------------- |
| `Optional`               | A variable may be of a certain type **or None** | Makes functions flexible (optional args)           |
| `_import_ex00_loader()`  | A helper that **imports `load()` at runtime**   | Avoids errors and bad practice (I/O on import)     |
| `DatasetView` + `.raw()` | Wrapper around pandas DataFrame                 | Gives nice printing but keeps real data accessible |

---


## ex02

```
| Function / Syntax                                         | Usage / Explanation                                  |
| --------------------------------------------------------- | ---------------------------------------------------- |
| `os.path.join(a, b)`                                      | Joins paths safely for any OS.                       |
| `os.path.dirname(__file__)`                               | Returns folder containing current script.            |
| `[c for c in countries if c not in df["country"].values]` | List comprehension to check missing countries.       |
| `df["country"].isin(countries)`                           | Returns Boolean Series where country is in the list. |
| `df[...]`                                                 | Select rows where condition is True.                 |
| `tens = {"k":1e3, "m":1e6, "b":1e9}`                      | Dictionary mapping suffix → multiplier.              |
| `isinstance(x, (int, float))`                             | Check if value is numeric.                           |
| `x[:-1]`                                                  | All characters of string except last one.            |
| `x[-1].lower()`                                           | Last character of string, lowercase.                 |
| `float(x[:-1]) * tens[x[-1].lower()]`                     | Convert `'2.5M'` → numeric value.                    |
| `int(float(x))`                                           | Convert numeric string → int.                        |
| `df.melt(id_vars, var_name, value_name)`                  | Convert wide → long dataframe.                       |
| `.assign(col=lambda d: ...)`                              | Add/transform column using a function.               |
| `.map(func)`                                              | Apply function to each element in a Series.          |
| `.dropna()`                                               | Remove missing values from DataFrame.                |
| `.astype(int)`                                            | Convert data type.                                   |
| `.between(a, b)`                                          | Boolean mask for values between a and b inclusive.   |
| `sns.lineplot(data, x, y, hue)`                           | Plot line chart from DataFrame.                      |

```

### Population Data Flow
```yaml
CSV File: population_total.csv
+---------+------+------+------+ ... +------+
| Country | 1800 | 1801 | 1802 | ... | 2050 |
+---------+------+------+------+ ... +------+
| France  | 1.2M | 1.3M | 1.3M | ... | 67M  |
| Australia| 0.2M| 0.21M|0.22M | ... | 26M  |
+---------+------+------+------+ ... +------+
        |
        v
  load_csv.load()
  ---------------------
  Output: pandas DataFrame
        |
        v
  Filter for selected countries
  df[df["country"].isin([country1, country2])]
        |
        v
  Extract country names
  country_names = [row[0] for row in filtered df]
        |
        v
  Flatten & unpack numbers
  - Convert "1.2M" → 1_200_000
  - Convert "26k" → 26_000
  - Keep numeric as-is
        |
        v
  Reshape: Wide → Long (pd.melt)
  +---------+------+------------+
  | Country | Year | Population |
  +---------+------+------------+
  | France  | 1800 | 1200000    |
  | France  | 1801 | 1300000    |
  | ...     | ...  | ...        |
  | Australia | 1800 | 200000   |
  | Australia | 1801 | 210000   |
  | ...     | ...  | ...        |
  +---------+------+------------+
        |
        v
  Filter years 1800–2050
        |
        v
  Render plot (Seaborn)
  - X-axis: Year
  - Y-axis: Population
  - Hue: Country
        |
        v
  Line chart output:
  France population ↑
  Australia population ↑

```

## ex03

### functions / syntax used:
```
| Function / Syntax                           | Usage                                        | Explanation                                                                 |
| ------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------- |
| `sns.scatterplot()`                         | Plot a scatterplot                           | `x`, `y` define axes; `hue` colors points; `legend` controls legend display |
| `legend=False`                              | argument in scatterplot                      | hides the legend                                                            |
| `hue='Country'`                             | argument in scatterplot                      | color-code points by country                                                |
| `zip(iter1, iter2)`                         | combine two iterables for parallel iteration | iterates over pairs `(df, name)` simultaneously                             |
| `pd.merge(df1, df2, on="col", how="inner")` | merge DataFrames                             | inner join on `"col"`, keeps only common rows                               |
| `.dropna()`                                 | DataFrame method                             | removes rows with any missing values                                        |
| `.assign(new_col=lambda d: ...)`            | DataFrame method                             | create or modify column using a lambda function                             |
| `lambda x: ...`                             | anonymous function                           | used inside `assign` to apply transformation on column values               |
| `x[:-1]`                                    | string slicing                               | all characters except the last                                              |
| `x[-1]`                                     | string indexing                              | last character of string                                                    |
| `isinstance(x, str)`                        | type checking                                | check if `x` is a string                                                    |
| `tens = {"k":1e3, "m":1e6, "b":1e9}`        | dictionary                                   | maps shorthand letters to multipliers                                       |
| `df[['col1','col2']]`                       | select columns                               | creates a new DataFrame with only selected columns                          |
| `.rename(columns={old:new})`                | rename column                                | change column names for clarity                                             |
| `-> None`                                   | type hint                                    | indicates function does not return a value                                  |

```


### data flow for GDP + Life Expectancy


```
          +----------------+               +----------------+
          | df_life        |               | df_gdp         |
          |----------------|               |----------------|
          | country        |               | country        |
          | 1800           |               | 1800           |
          | 1801           |               | 1801           |
          | ...            |               | ...            |
          | 2020           |               | 2020           |
          +----------------+               +----------------+
                  |                                 |
                  | slice columns: ['country', year]|
                  | rename year column               |
                  v                                 v
          +----------------+               +----------------+
          | df_life_year   |               | df_gdp_year    |
          |----------------|               |----------------|
          | country        |               | country        |
          | Life Expectancy|               | GDP            |
          +----------------+               +----------------+
                  \                               /
                   \                             /
                    \ pd.merge(on='country')    /
                     \ (inner join, common countries)
                      \                         /
                       v
                  +----------------+
                  | df_merged      |
                  |----------------|
                  | country        |
                  | Life Expectancy|
                  | GDP            |
                  +----------------+
                           |
                           | .dropna() → remove rows with missing values
                           |
                           v
                  +----------------+
                  | df_cleaned     |
                  |----------------|
                  | country        |
                  | Life Expectancy|
                  | GDP            |
                  +----------------+
                           |
                           | .assign(...) → transform columns
                           |   - GDP: convert '1.2M' → 1_200_000
                           |   - Country: copy 'country' for plotting
                           v
                  +----------------+
                  | df_final       |
                  |----------------|
                  | Country        |
                  | Life Expectancy|
                  | GDP            |
                  +----------------+
                           |
                           | pass to Seaborn
                           v
                  +----------------+
                  | scatterplot()  |
                  |----------------|
                  | x = GDP        |
                  | y = Life Exp   |
                  | hue = Country  |
                  | legend = False |
                  +----------------+
```

### **Key Steps**

1. **Slice Columns** → only keep `'country'` + target year.
2. **Rename Columns** → make column names meaningful (`Life Expectancy`, `GDP`).
3. **Merge** → inner join to keep only countries present in both datasets.
4. **Drop NA** → remove incomplete rows.
5. **Assign / Transform** →

   * Convert GDP shorthand (`1.2M`) into integers.
   * Copy country column to `Country` for plotting.
6. **Plot** → Seaborn scatterplot with `x=GDP`, `y=Life Expectancy`, `hue=Country`.

---

Perfect! Let’s zoom in on **how `unpack_numbers` transforms GDP strings** and connect it to plotting.

---

### **GDP Conversion Flow with `unpack_numbers`**

Suppose you have a GDP column like this (strings):

```
df_gdp[year] = ['1.2M', '3.5B', '980k', 5000]
```

---

### **Step 1: Define conversion dictionary**

```python
tens = {"k": 1e3, "m": 1e6, "b": 1e9}
```

* `'k'` → thousand
* `'m'` → million
* `'b'` → billion

---

### **Step 2: Define `unpack_numbers`**

```python
def unpack_numbers():
    return lambda x: int(float(x[:-1]) * tens[x[-1].lower()])
                   if isinstance(x, str) and x[-1].lower() in tens
                   else int(x)
```

**Logic:**

1. Check if `x` is a string **and** last character is in `tens`.
2. `x[:-1]` → numeric part, e.g., `'1.2M'[:-1]` → `'1.2'`
3. `x[-1].lower()` → suffix, e.g., `'M'` → `'m'`
4. Multiply numeric part by the dictionary value → convert to integer.
5. Else, if `x` is already a number, just convert to `int(x)`.

---

### **Step 3: Apply conversion**

```python
unpck = unpack_numbers()
df_gdp['GDP'] = df_gdp[year].map(unpck)
```

**Example transformation:**

| Original | Step        | Result       |
| -------- | ----------- | ------------ |
| `'1.2M'` | `1.2 * 1e6` | `1200000`    |
| `'3.5B'` | `3.5 * 1e9` | `3500000000` |
| `'980k'` | `980 * 1e3` | `980000`     |
| `5000`   | int(x)      | `5000`       |

---

### **Step 4: After conversion → ready for plotting**

```
df_gdp['GDP'] = [1200000, 3500000000, 980000, 5000]
```

* Now all GDP values are **numeric**, so Seaborn can plot them on the x-axis.
* Each country’s GDP corresponds directly to a life expectancy value for plotting.

---

### **ASCII Mini Diagram**

```
Raw GDP strings:
['1.2M', '3.5B', '980k', 5000]
           |
           | map(unpack_numbers)
           v
Converted GDP integers:
[1200000, 3500000000, 980000, 5000]
           |
           | merge with Life Expectancy
           v
df_final:
Country      GDP          Life Expectancy
France       1200000     82.5
USA          3500000000  79.1
Italy        980000      83.2
SomeLand     5000        45.0
           |
           | pass to sns.scatterplot
           v
Scatterplot:
x-axis = GDP
y-axis = Life Expectancy
color = Country
```
