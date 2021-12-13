# 5.2.1 Tuples are used for grouping data
year_born = ("Paris Hilton", 1981)
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress",
    "Atlanta, Georgia")

julia[2] # 1967
julia[0] = "X" # TypeError: 'tuple' object does not support item assignment
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
julia # ("Julia", "Roberts", 1967, "Eat Pray Love", 2010, "Actress", "Atlanta,
      # Georgia")

tup = (5,)
type(tup) # <class 'tuple'>
x = (5)
type(x) # <class 'int'>