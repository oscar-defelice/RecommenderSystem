###
### DaMa.py
###
### Created by Oscar de Felice on 14/01/2020.
### Copyright © 2020 Oscar de Felice.
###
### This program is free software: you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version.
###
### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
###
### You should have received a copy of the GNU General Public License
### along with this program. If not, see <http://www.gnu.org/licenses/>.
###
########################################################################
###
### DaMa.py
### This module contains objects to convert datasets into a matrix of
### features.
###
### 14/01/2020 - Oscar: Created the module
### 05/02/2020 - Oscar: DaMa CaVect object created
### 05/02/2020 - Oscar: CaVect __init__ method defined
###

"""
DAta to MAtrix module.

This module contains objects to convert datasets into a matrix of features.
"""

class CaVect(object):
    """
        CaVect object.

        Object collecting methods to convert categorical variables to numerical
        vectors.

        Parameters
        ----------
            data                    : pandas dataframe
                                        It contains the data of users.

            feature_categories      : list of strings
                                        It contains the list of columns containing categorical variables.

            feature_vect_categories : list of strings
                                        It contains the list of columns containing categorical vector variables.

        Attributes
        ----------
            df_         :   pandas dataframe
                                It contains the original user dataframe.

            X_          :   numpy array
                                It contains the matrix of user features.

            auth_ids    :   list of strings
                                It contains the list of user ids.


    """

    def __init__(self, feature_categories, feature_vect_categories):
        """
            Constructor method.
        """
        super(CaVect, self).__init__()
        self.arg = arg
