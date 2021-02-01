def df_firstclean (df):
    
    #Firstly we will delete every column that gives us no information.

    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df.drop(empty_cols,
            axis=1,
            inplace=True)

    # Get rid off the columns that have less than  75% of rows filled.
    ''' This can seem a bit repetitive with the previous function but doing it separately 
    allows us to use only one or  the other in future ocsasions.'''
    perc_null = df.isnull().sum().apply(lambda x: x/df.shape[0]).sort_values(ascending=False)
    column_null_75 = perc_null[perc_null > .75].index
    df.drop(column_null_75, axis=1, inplace=True)

    # Duplicate columns
    def get_duplicate_columns(df): 
    
        ## Create an empty set 
        duplicate_column_names = set() 
        
        ## Iterate through all the columns of dataframe 
        for x in range(df.shape[1]): 
            
            ## Take column at xth index. 
            col = df.iloc[:, x] 
            
            ## Iterate through all the columns in dataframe from (x + 1)th index to last index 
            for y in range(x + 1, df.shape[1]): 
                
                # Take column at yth index. 
                otherCol = df.iloc[:, y] 
                
                ## Check if two columns at x & y index are equal or not, 
                ## If equal then adding to the set 
                if col.equals(otherCol): 
                    duplicate_column_names.add(df.columns.values[y]) 
                    
        # Return list of unique column names whose contents are duplicates. 
        return list(duplicate_column_names)

    duplicate_column_names = get_duplicate_columns(df)
    df.drop(duplicate_column_names, axis=1, inplace=True)

    # Delete the empty rows

    df.dropna(axis=0, how='all')

    clean_df = df

    return clean_df


# Creating a new dataframe only with some rows that have an specific value in a column.
def columnvalue_filter (df,col_name, col_value):
    filtered = (df.loc[df[col_name] == col_value]).copy()
    return filtered
