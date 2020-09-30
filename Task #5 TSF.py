{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task # 5 - To explore Business Analytics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Perform ‘Exploratory Data Analysis’ on the provided dataset ‘SampleSuperstore’"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Importing essential libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"C:/Users/krish/OneDrive/Desktop/TSF/SampleSuperstore.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Check Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Ship Mode</th>\n",
       "      <th>Segment</th>\n",
       "      <th>Country</th>\n",
       "      <th>City</th>\n",
       "      <th>State</th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Region</th>\n",
       "      <th>Category</th>\n",
       "      <th>Sub-Category</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Bookcases</td>\n",
       "      <td>261.9600</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>41.9136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Chairs</td>\n",
       "      <td>731.9400</td>\n",
       "      <td>3</td>\n",
       "      <td>0.00</td>\n",
       "      <td>219.5820</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Second Class</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>United States</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>California</td>\n",
       "      <td>90036</td>\n",
       "      <td>West</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Labels</td>\n",
       "      <td>14.6200</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>6.8714</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>957.5775</td>\n",
       "      <td>5</td>\n",
       "      <td>0.45</td>\n",
       "      <td>-383.0310</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>22.3680</td>\n",
       "      <td>2</td>\n",
       "      <td>0.20</td>\n",
       "      <td>2.5164</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Ship Mode    Segment        Country             City       State  \\\n",
       "0    Second Class   Consumer  United States        Henderson    Kentucky   \n",
       "1    Second Class   Consumer  United States        Henderson    Kentucky   \n",
       "2    Second Class  Corporate  United States      Los Angeles  California   \n",
       "3  Standard Class   Consumer  United States  Fort Lauderdale     Florida   \n",
       "4  Standard Class   Consumer  United States  Fort Lauderdale     Florida   \n",
       "\n",
       "   Postal Code Region         Category Sub-Category     Sales  Quantity  \\\n",
       "0        42420  South        Furniture    Bookcases  261.9600         2   \n",
       "1        42420  South        Furniture       Chairs  731.9400         3   \n",
       "2        90036   West  Office Supplies       Labels   14.6200         2   \n",
       "3        33311  South        Furniture       Tables  957.5775         5   \n",
       "4        33311  South  Office Supplies      Storage   22.3680         2   \n",
       "\n",
       "   Discount    Profit  \n",
       "0      0.00   41.9136  \n",
       "1      0.00  219.5820  \n",
       "2      0.00    6.8714  \n",
       "3      0.45 -383.0310  \n",
       "4      0.20    2.5164  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Ship Mode', 'Segment', 'Country', 'City', 'State', 'Postal Code',\n",
       "       'Region', 'Category', 'Sub-Category', 'Sales', 'Quantity', 'Discount',\n",
       "       'Profit'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 9994 entries, 0 to 9993\n",
      "Data columns (total 13 columns):\n",
      "Ship Mode       9994 non-null object\n",
      "Segment         9994 non-null object\n",
      "Country         9994 non-null object\n",
      "City            9994 non-null object\n",
      "State           9994 non-null object\n",
      "Postal Code     9994 non-null int64\n",
      "Region          9994 non-null object\n",
      "Category        9994 non-null object\n",
      "Sub-Category    9994 non-null object\n",
      "Sales           9994 non-null float64\n",
      "Quantity        9994 non-null int64\n",
      "Discount        9994 non-null float64\n",
      "Profit          9994 non-null float64\n",
      "dtypes: float64(3), int64(2), object(8)\n",
      "memory usage: 1015.1+ KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Ship Mode       0\n",
       "Segment         0\n",
       "Country         0\n",
       "City            0\n",
       "State           0\n",
       "Postal Code     0\n",
       "Region          0\n",
       "Category        0\n",
       "Sub-Category    0\n",
       "Sales           0\n",
       "Quantity        0\n",
       "Discount        0\n",
       "Profit          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "      <td>9994.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>55190.379428</td>\n",
       "      <td>229.858001</td>\n",
       "      <td>3.789574</td>\n",
       "      <td>0.156203</td>\n",
       "      <td>28.656896</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>32063.693350</td>\n",
       "      <td>623.245101</td>\n",
       "      <td>2.225110</td>\n",
       "      <td>0.206452</td>\n",
       "      <td>234.260108</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1040.000000</td>\n",
       "      <td>0.444000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6599.978000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>23223.000000</td>\n",
       "      <td>17.280000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.728750</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>56430.500000</td>\n",
       "      <td>54.490000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>8.666500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>90008.000000</td>\n",
       "      <td>209.940000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>0.200000</td>\n",
       "      <td>29.364000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>99301.000000</td>\n",
       "      <td>22638.480000</td>\n",
       "      <td>14.000000</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>8399.976000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Postal Code         Sales     Quantity     Discount       Profit\n",
       "count   9994.000000   9994.000000  9994.000000  9994.000000  9994.000000\n",
       "mean   55190.379428    229.858001     3.789574     0.156203    28.656896\n",
       "std    32063.693350    623.245101     2.225110     0.206452   234.260108\n",
       "min     1040.000000      0.444000     1.000000     0.000000 -6599.978000\n",
       "25%    23223.000000     17.280000     2.000000     0.000000     1.728750\n",
       "50%    56430.500000     54.490000     3.000000     0.200000     8.666500\n",
       "75%    90008.000000    209.940000     5.000000     0.200000    29.364000\n",
       "max    99301.000000  22638.480000    14.000000     0.800000  8399.976000"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Computing Pairwise Correlation of Columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Postal Code</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Discount</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Postal Code</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.023854</td>\n",
       "      <td>0.012761</td>\n",
       "      <td>0.058443</td>\n",
       "      <td>-0.029961</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sales</th>\n",
       "      <td>-0.023854</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.200795</td>\n",
       "      <td>-0.028190</td>\n",
       "      <td>0.479064</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Quantity</th>\n",
       "      <td>0.012761</td>\n",
       "      <td>0.200795</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.008623</td>\n",
       "      <td>0.066253</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Discount</th>\n",
       "      <td>0.058443</td>\n",
       "      <td>-0.028190</td>\n",
       "      <td>0.008623</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.219487</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Profit</th>\n",
       "      <td>-0.029961</td>\n",
       "      <td>0.479064</td>\n",
       "      <td>0.066253</td>\n",
       "      <td>-0.219487</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Postal Code     Sales  Quantity  Discount    Profit\n",
       "Postal Code     1.000000 -0.023854  0.012761  0.058443 -0.029961\n",
       "Sales          -0.023854  1.000000  0.200795 -0.028190  0.479064\n",
       "Quantity        0.012761  0.200795  1.000000  0.008623  0.066253\n",
       "Discount        0.058443 -0.028190  0.008623  1.000000 -0.219487\n",
       "Profit         -0.029961  0.479064  0.066253 -0.219487  1.000000"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2eaaca990f0>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (12,8))\n",
    "sns.heatmap(data.corr(),annot = True, cmap = \"BrBG\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Visulization"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Shipping Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Standard Class    5968\n",
       "Second Class      1945\n",
       "First Class       1538\n",
       "Same Day           543\n",
       "Name: Ship Mode, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['Ship Mode'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([0, 1, 2, 3]), <a list of 4 Text xticklabel objects>)"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(6,7))\n",
    "sns.countplot('Ship Mode',data = data, palette = 'Blues_d')\n",
    "plt.title('Popular Shipping Modes',size=14)\n",
    "plt.xlabel('\\n Shipping Mode', size=12)\n",
    "plt.ylabel('Numer of Orders', size = 12)\n",
    "plt.xticks(fontsize=10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### *As we can see, the standard class shipping has the most count which means the customers have opted for this type of shipping mode the most. This is because Standard class delivery will cost very less compared to the delivery for same day. Hence, customers choosing same day delivery is the least.* "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Shipping Mode Vs Count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x2eaad5332e8>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 529.875x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot('Ship Mode', data= data, hue = 'Segment',kind='count',palette='plasma',aspect= 1.0,height= 6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Category Vs Sales Bar Graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Sales')"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar('Category','Sales',data=data)\n",
    "plt.title('Sales Vs Category',size=15)\n",
    "plt.xlabel('Category',size=13)\n",
    "plt.ylabel('Sales',size=13)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Quantities Ordered by each Segment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Segment</th>\n",
       "      <th>Quantity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Consumer</td>\n",
       "      <td>19521</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Corporate</td>\n",
       "      <td>11608</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Home Office</td>\n",
       "      <td>6744</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Segment  Quantity\n",
       "0     Consumer     19521\n",
       "1    Corporate     11608\n",
       "2  Home Office      6744"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grp = data.groupby('Segment') ['Quantity'].sum() .reset_index()\n",
    "grp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiEAAAFtCAYAAADRZboNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nOzdeXzbdf3A8dcnV9O0Tbutu6+OrYwrbANGuQ85BIcIiIgiDsQDFQ+8fqj4S6OoUzz4eYKCUgT9gYCI7qeACiIg95BxjLXbugPGNna0690mn98fn2+aLEtztEm+Sfp+Ph59tN82+eadNPl+39/351Jaa4QQQgghCs1hdwBCCCGEGJ8kCRFCCCGELSQJEUIIIYQtJAkRQgghhC0kCRFCCCGELSQJEUIIIYQtJAkRQgghhC1c2d5BhZQXWA6cAywCJgMDwBvAo8AdOqgfTXH/U4CHrc1TdVA/kubxHgFOBv6pg/qUNLc9GHjF2uwBpuug7kxzn2YgGHefRh3Ub4xw2wZgQ3zsCc9nNObpoG5XIXUZ8Ov43yU8djswF2jRQX1ZpjtPdb+Ex8w41oR9KOBC4P3AEcAUIAxsA7YCTwP/Av6e7n+RigqpWuDDwNnAwUA90A1swbz+t+mgfi7NPpJNiqOBLqDdivOnOqhfSXK76D5uxbz/40WsfXQA64FVwIPAAzqoIyn2dQrZvXf2+byk+P8NAbsxn4X7gZt0UHeniCObyYJCOqib4+7bQOwzEa8f6ATeAl7EvA/u1EH9ehaPtZ+440Gi6P9xPfA34Mc6qDfG3U8B/wBOAdqAxaleE+s+fwDOwxzbAjqod2UQ3+nAQ5k8F8uJOqgfS7E/F+Y9PtX6VdpjZpJ9nAhcBJwEzARqMa/VRuBJ4C7gYR3cd9IoFVJbrNvfooP6w2ke4zrgq0BYB3XW5xVrHw3Ax4HTgAVAFbATcyxpxXw+H9ZB/WLC/RZYf8/UpTqob08RxzHAe4ETgdnABMz7eTvmvfwIcI8O6i1J7usCBuN+9ZIO6kCqYFRIHQs8Efer/V5vFVIfBn6Zaj8JZsfHF/f/AXPcnK+DetsI8cS/nifqoH5sFO/rlPHEy+rNokLqDOBXwKy4X3cCFcBB1tdHVUj9CViug3r36OIdtSvifvYB7wNuyuL+PkxC8rEs7jOA+ZAkMxFwY96UIx3Awlk8Vj69RfpY9vm7Cqk64D72PSkMYZK5OcABwPHA1cDlwK2jCUyF1CXAjzCvZ9QeoBoIWF+fUiH1G+BKHdS9aXbZjTkIAziBSXH7+YgKqSt1UP8qzT4iwI647SrMAWs25vX4LLBZhdTVOqjvSbMvMEnDQJrbpPp7/P/Ph7k4ONn6+qQKqbfFn5RHEP+6jCTV3zuB6GvvBOqsOA7GHNS/q0LqTuAzOqjfSvM46SR+ptyY98ci6+sTKqTerYP6LwA6qLWVtL2IOcF9F/jkSDtXIXUpJgEB+HAmCUgSu9j3hJRMuv/5OcQSEDDHuEcyeXAVUjOAFuD0uF9HMMlyNbHX6mPAcyqkLtJBvT6TfeeaCqkPAjcClXG/7sTEORU4HHg3sA7z/xtJB9CX5uGSHh+s1+vXwJlxv9bWPt2Y49kBmPfF91VI3Q5cnpi8JThMhdRSHdTPpLjNh9LEm2gH5v+YSqpjeRXw36R4/yfRT/rz3ADmOJZVPBknISqkLgLusO7zOuZkfW800VAhdRDmzXwV8E7gCRVSJ+ig3pnpY4yFCik3cKm1+WPgU5gPbDZJCMCHVEh9Xwf12kxurIP6CWDaCDE9gjkJPJGuilMEliZWOTJwG+b5hYEbMK/1Oh3UEeuK4BDgLEyVZFRUSH0e+J61uQbz4fk/HdTd1tXtEuDTwAetr4UqpE5Nk4h8L+FqvsKK88eYJOImFVKP66B+LcU+NuugbkiI1YM5WC7DXNHNBu5WIfVtHdRfSfNUL8j2CjfBPv8/FVJTMK/LVzEHztsxV3ap7PO6jMJndFDfGv8LFVLTgWOJVbHeD5yiQur4Ubzf4u33mbKqtO8CfopJLG9XITUnWvHQQb1RhdTVwC3Ax1VI3aeDer+rOxVSMzFJL8AvoonMKLwrVZUjQ9ELq59gThrvViF1lQ7qjlR3sq5m/wnMwJwcfolJSJ7XQR22PjsHYJKczwJHYj6vBU9CrMrDrzHdA14Avg48GP2/qZCajLmYOR/zeU/lqlRVjhQxHIh5vaZhXq9fAb8BntVBPWDdphrzXj4fc6xZjnlfD42w23agAXMBljQJUSHlw1SpNLAZc/GWzhEjVRWy8BEVUj/QQb0ukxvroP4XI5/nHsP8f/6lg/r0ZLdJJaMkxEowfmXdfjVwmg7q+KtAdFCvAa5WIfUQ8AdMVaQF8yYvhHdimgLWAF/G/OOXqpA6TAf1SxncfzMmizsc+BamiUGMQIVUI+Y1B7hWB/WK+L/roB7CXHW+iLkCriRLKqROxVyxgimlv1MHdU/cY2jgeeAy64PwS6AJc8C+ggzpoO4H/qhCahemSdGFOcCkSxwS9zMAPAs8q0LqJ8DvgVOBL6uQekkH9W+z2d9Y6KDeDlxrJQEfAk5QIXVgpsl1DuPYCtwL3GtdyNyOOTGuVCG1yHqf5Oqx+oA7rQuS32Cu0E4C/hJ3m1+pkDoP8979lQqpgA7qPQm7ugVTxVkPfD5X8WXLujI/G3OSuw5YDJyAqfDemOJ+XsxrPgNzFX9OYjJkfXbWAf+jQupnmOTerqrs1ZgEZCtwkg7qvfF/tM419wH3jeY4ko61z/swJ9ndwDId1P9OvJ0O6i5Mk8RDKqT+G/ghJnkYyW2Y1/V9KqQ+Z70/E10I+DFNiJVkloSMxQZMpfpQ4JvAxXl+vLQy7Zj6TUwJpx94T2ICEk8H9f9hPjAAy6y2pEKInnRarAz6noTfpxPBJC9grjaOzmVwZWhx3M9/THfjDJpIkrke8x7dAbw3PgFJsv+bMYkywOUqpA4bxeM9hmmSAPMhHTWrAngBpmoIcJ11ciy0v8b9PKbnNFY6qO8iltgdwv59a3Llhbifq5P8/SOY5qtZxCoeAKiQ+hjwdszx4DLrxGOX5ZhmrQes9vsW6/fpjmkfwTQtAnw8XTVGB/WgDuqvAQ+MJdgxiB5LHk5MQBKN8jiSzscwTYZgmt72S0CSxPGWDupLdVCnStxaMceUOkz1JJloU0w2ffPGIkLsM3iRCqkjCvS4I0qbhFhXUtG20d+lKVFH/RCIvpmuGmVsGbPKp9EDR7QUF/3AfsAqk6dlJVD/tDZXpLqt2Mes9DfJjgqpJkyJGExn0Uz6EHwD8x5QwCfGGIJzjPfHusK+wdqcR/rmkHxQcT+P+TnlwE8wCQDkLwlZFPfzfscr64T+cWvzUhVS5wOokJpHrOnvB1YJ2k7RE9Rt1ve7MP0ZjlIhdXiK+0WPuWt0UP8u0wdL1Ym6QHJ+HMlQtG/ESzqo783xvqPJxeWJf1AhdQCmUteBaT0oCB3U9wOPY44Ntp/nMqmEnBJ3u0w62EXLVg9amyerkMr3UODLMAfYh+Payh7B9P6uB87NYl//ZX0/VYXUWbkKsAw9Q6wU+X2rTTWX3hb3c6bvu3bMyBQwzSDZOhFT8YPctY2vjPs52aiOfIt/D9vS6TCeVZL+h7XZZDUd5IQKqQoVUu/GXASB6VfwYrLb6qC+G9PHDUwfoGmYE0Y18DJwba7iGg0VUidjOmB2YEY4oc3osvusmyTtzKhCahYQ/Szel+w2Rehp6/tJKqQ+U8iKoQqp2cQ6ut6fh4e4C1NdPU2FVGJTy+WYROB3earwpBI9z51RwNaKpDLpExJfwl014q329wKmN3Mdpp2rPYv7ZszqYBXNMqPVj2hv+NsxHfOuAO7OZH86qJ+yhuadD3xbhdQDaXo/l4tnVEilKi0+oYP6guiGNsOKbyZW+l2jQuoF4N/Ac5gDy8tjeO2i77sBYsOuM/ECpoKyUIWUK5M+BwkdU6NuzeIxU1mDeQ4eYH6K292rQirVSInNOqiXZvqgVme+TxP7bPxHB/Xzae72BRVSV6a5zVId1JszjWME/8F0xvNgrn7bRrGP41RIvRm3HR0dA6Z/13eB5jT7uApzkTUTk1TPwoxm+aDVT2is/qhCKtXomA06qI8d4W/RJpc7E/oS3IbpE/IBFVJfinaajDPa43Uq71chla5vX7Jmr0x9G3O8rcJUDoNWp/7nMH2snkzXETfOT1RIfS/F34d0UMdXXOJfrxcSbzxWOqi7VEj9HnOhvBxTrcW6MI9WArNtinlehVSqqtWjOqgvShPX49Yo1ncCK6wRPLac5zJJQibF/ZzNSJf48vkk8pSEYA4i8zHZZmIprQWThJypQmpWFj2Kv4KpnizGfOAL1qHQRvVp/j4xye8+AbwJfA5zAFnCvr3Xt6uQugP4jh5hTHoK0ffd7izLxNH3ncLEvD3JbeJPttEhuvHNFl/I4ISdESsZ3o0ZZpjsNYyakGZX6YYdxieRPqAm7m9vApekuT+Y/2FVmtvkokknfrhrqtckFTf7Dl2NV2vtt5YRhmOCaS5TIfUhTF+I6InpG7n635P+uSXtb6JCyo+5gINYU0zUQ5gOnNFm8rsS/h5/vB7NsOJkKtl36GxO6aB+xar83IS5gJiASUqi/SgiKqQexTSR/SnN7mqtr5EkXmhl9HqpkHo54bZRK3RQ35Dk9/F+hUlCLlMhdZ11sj8dM3ruZR3UT6e6cxKT0/w908/UlzEj+Y4E3sP+76WCGNWkMhmKP6hX5PFxolcM9+iEyYd0ULeqkPo3ZljVZcQ6zKakg3qNCqlfY4ZffUOF1O91UKcb71/q9puILB2ryvDfKqS+j8moTwaWYjp5eTCjla7GtLsvG8WHDVL3Pk9Gpb/JiCfb3ZiRBE8k+dtYZBJT1pNQJRgpiXwIuFBnNlHcPhOR5VEmr0c6+01eaJ28l2IqIB8G3q5C6jQd1CNOZKWD+kEVUn/GjOJ7E3NVnispJyJL4f2YRHKdDurH4/9gDa+9Hfgipkkm8cQR/9rm6so2m8nKRkWbiQaPUiG1FHgHcAzmgmYqpjvAKZih3bcAH0lx1Z5yIrIxmEryJCRtBUgH9b9USLUCjZhj5COMrUPqiBN/ZUMH9csqpG7DOjeqkLo3l6PVMpVJX4346keyf8JI4m+bl0nLlJlFM9pEkHjFEBVtovmQ1XSTqWbMVdQBQLoS9bimg7pDB/XtOqg/ooN6MeZK5AwgetVSD9yTZft/9H03Mcs+RZlc2YR0UCsd1AqTjBxtxToBuNUaGpkT1nsuemWWzzlz5sU9p6mYE9kWzP/hW3l83NGIr/rk7DXRQd2pg/rvmJPYRqw5XzK4a7TU323HQTiJ6AnqNyP8PXpMOyNJP4PECnRJ0UH9jA7qkA7qs3VQT8Mcf79E7H1yBdlNJplO/PtvxAqCDur66OfL+oxlO/Pvrdb3y1VITcBUsYYY+X9cKEHMqNdGTNN6wWVycI9vj89mOE+0LD/Evh3i4sujmZT4fEnuF/X+uH38TYWUTvwiNp5+Hll0VtRmeuloH4FrrYlqRAZ0UPfpoP6bDupziR0wZ7FvJ8l0ou87D9kNLY2+717L5ISig7pHm9kMzwP+jvkw3pFlwprKQcQqgRlNDDRWOqi3W6MizsB8bj6pzGyhxSI6eqWf7A/maVnDPO+0Nk+1RviVBBVSAUw1B6B5hGNadN4jB+YqNt7LcT+nm9ir6Omg3qCD+nrMsTvaTydlVSZL8a/X4hFvNXa3YUbuXYhJoiqAldrM52MbHdSbMJP7galqp2uOzblMkpCHiU0R++5UN4yyTthnWJv/TujkFZ+pz8xgd9HbJJubJOMJqSzZTo/7bUwVZwo2TlpU4n4R9/PCLO7397ifM33fzSN2IPlHqtsmsvqdfByTNJ9C7ibxWRb38yM52mdGtJlA8Hpr83qrucJWVjUsOvLpSZ18AqdciJ+iviFPj5EP2R7TLo9PmK0yfXRCuvOS36X06KBeTWx9lWyOI+n2u5lYx+hsRlFm+zhbME2jPiBk/bpQc4Ok801MNXAaZvbcgkqbhGgz42F0qNfFKqQyeQNcTaxjXEvC39YTa545IdVOrJNKtDT+XMLfFhGbR2Kp9XgjfUVnP323MuudZMSa5yE6jvrzmGREZCe+813GIw50UD+FmQ0VzJV8uo6zYIZVRt/TP8/0seIes5XYsM3rlJl6ftSs99pnrM11mImLCu0HmANMPfAFGx4/0VXE+q/cmsfHiR8BkXKhumJhzWf0AWvzM6Q+ps3FdLJsYN/h7BC7sj1IhdT7snj8Yl9VPXosycXIpXjR1+swFVIXpLzl2EQnU/RgOsyvTHHbgtFmXaTozNRfosDNeJm+6b6GKetWAL9PdUJQIXU2sTH2a0joq2F1KPq9tfkeFVKphi1eY30fYv/JXKJXDGt0UD+rg7prpC/gz5gDsZfs1zH5EaZtvQab5w4oJiqk5mU4N0j8hFTZjjr4EqYKV4+ZjnvE5jsVUlcQq3Tdal05jca3rcc8gCQTDGVKhdREzPwm0ZPhV+3ob2ANbYweZD+rQsq2fgIqpN5DrH/KS8QmFsz141QQ6yvWRZIJy4rUeZgTQBj431THNKuM/oh1v8TqyS+INTP8XIXU8akeVIWUS4VUCDPhY8GpkDotXcJvzecRTbZyNXop6ibMuQrgZmVWtc2HP2Iqk9/HrLNUDP2Pom7AjLryM4YOxqOR0ZWeNYTqw5iEIgCsUiEVXcBuDwwvAHQlZuE4F+akf/EIo0q+iRkSNAF4WIXU5zCLkvXE7euLxNr+brA+dFh/ryA25DDtsCId1P0qpO7HLHD3IeBnmTxv6759KqSagZuJrZVip4oMqgJdeSxzRx2KmQfhr5j290ejo2usyYYOw8xTcZl1+6fJshKgg/rvKqS+DHwHcwB6Xpk1G1bGvVeiC9hFk51nyW51yMTHfE2F1L2Y6tm1KqRakszFkJT1vKML2H2C2BDS63RQ3zniHfPvBkyZtQbzubom9c1zR5lJwI7DnCjfYf36dcwopJwfhFVIHYJJdKIV25/q3Mz5UQjRZOKfGfYVuAuz7P35KqQmaGsxUeuYdQGxBdn+oULqF8QWsIvAcKX5HZjK9XzsO759H9MB/Q7MBePz2pq8y0qaL8BcAFbF3T5ndFD3qpB6F7HX6xEVUskWsKvANPdewsjDw1M9Tj/mwqro6KDusRLRGynw+yDjcrMO6t9a8x3cgrm6uwW4RYVUB6ZCEj/yYT1mjZn/jLCvTdbkN/dgerD/HjMWfI+1H1/czW8htqZL1PnEejL/nsz8HpOEHKnMwllJYxvBrZhS9kFZ3CdfLiZ9f4WriU0Xnql0k5WByd6jJ9NBTCXtHdYXyky21YVJLuM7dj4PnK9HMS20DurvKjMp1f9gXv+7AG29V6owpc2o3wIf1SnWmMlQdAHDOZge4z9NcpvZat/JsioxJ/n4570J85plMnNlusnKwKxym2oipqR0UO9QIfVLTIn/KmVWz0w3f8pI9pm0LsH/qJCKNl86MKOC4v8/Ycz/6LNWCXgsEicrA/P6xx877sRUce2SbrIysOaZsEa5RGeuzPSYdi/mgipa4R1+n+qgXmsNd70N06nzKusrbB2zq9n3f/NvYh1eC20Qcx64xvrSKqQ6MfHFVz/7gc/poE61xk26ycoA7tBBvU8fP+v1OhJzrD8Dc0F9pRVLB2a4cy2x1oMwpk/HzemfXs6lm6wM4JM6qDOaaTrOLZg5n3I9+3VKWbV566D+i9V8cjnmam8RplQePw/Ib4Ar050IdFA/oczqvB/GjNE/FHPy6sN0rHoCMz492dVz9IrhVZ3ZCrlgJiTqwLyRrsBcPWfEGpv/FfafDK2cZNLnYviAoIP6AWVW0n0Hpm/PYZjktA6zSuMbmBkb7wV+P5oEJO6xblNmdr/o1fTBmLJ1N+a98ghm4cJnR/sYCY+3SoXU/1mP9RUVUrckqSw5iF0NaUzy9TomAX8es3DcQ1k873STlcHYZqX8HqbjbRXmQP+5JLfJZLKyVBMh+a0vMLPEdmI6lL8IPIWZ/fONLGJOJdlkZX2YVUKfwrwf/rrfvQork0mjov/TyzHvqTAZHmd0UL+lQuphTPJyBQnJstUZ8m0qpE4C3otZlmAm5n/UjRmB9m9M08+jmTxmnpyIeQ5vw/TvW4B57RTm/bMW09H81zqoN6TZV7rJyhjp79Z780wVUsdgLvROxCRH0fPSJsxsv49iplrfmvaZ5Ue6ycpgFJPL6aAeUiF1LQWetEzpHMzUqkLKiemz8U7Mif5tOnezDgohhBCiDOUkCQGwOg3+HTM76VvAyTqos1nzQwghhBDjSM6SEBjuRPQYpu1+K2ba4oJM0CSEEEKI0pLTJEQIIYQQIlPFPjmNEEIIIcqUJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhSQhQgghhLCFJCFCCCGEsIUkIUIIIYSwhcvuAIQQhddwzUoPMBeYAlRYX964nxO/4v+mgV3W1864r13AzvYVyzoL+VyEEKVLaa3tjkEIkWMN16x0ADOAecAB1vf4rxnkrxI6yP5JyjbgNWAN8CqwsX3FskieHl8IUSIkCRGihDVcs9INLAaagMOIJRlzAY+NoaXTC6wFnmhfsewTdgcjhLCHNMcIUUIarlk5GzgOk3QcAyzBNJWUmkpgEaZaklSgJXANMBV4wfp6ZfXy1YOFCU8IUQiShAhRxBquWTkLONX6OgVT5Sgnq1P87WJMohLVH2gJPAc8Yn09vnr56p78hSaEyDdpjhGiiFgdRt8OnItJPObbG1HefaR9xbKboxv+Jf7DgemOSsebsz4662mlVKompUHgGSQpEaJkSSVECJs1XLPSCbwNc+V/PjDB3ogKKrESciFwgHuiuzJNAgLgxjRNHQd8BRgMtASeBv4E3LN6+eq2nEcrhMgpSUKEsEHDNSsVcDwm8bgQ0/dhvNHAy9EN/xK/EzNqZ713tvfgUezPjXlNjwdWBFoC/wHuAe5evXz1qzmIVwiRY5KECFFADdesPAqTeFwEzLY5HLttaF+xrCtuux5QQMRT78lFUrbI+vp6oCXwKiYhuWf18tUv5GDfQogckCREiDxruGblgcClmORjgc3hFJMXE7aHEw9XrSvXlaGDgWuBawMtgbXAL4Ffr16+emeOH0cIkQVJQoTIk4ZrVh4P/JfW+hyllLI7niKU2B9kWvQHZ41zSh4f90DgeuC6QEvgHuDG1ctX/yuPjyeEGIEkIULkkNXX41yt9ZeUUscBSP4xosQkpBHodfgcHkeFo64Aj18BvB94f6Al8ApwE3Db6uWr9xTgsYUQSBIiRE5YQ2sv1Vp/USm1UBKPjCQmIQ1AV+Wcyik2vH6HAP+D6dD6v8D3Vy9f/XKa+wghxkiSECHGoOGalX7gSq31Z5VS0yX5yFgf0Brd8C/xezEdUzd6puakU+poVQKXA5cFWgJ/AL4hHVmFyB9JQoQYhYZrVs4APqu1vlIpVSPJR9ZebV+xLBy3PQUIA7gnuvPZHyRTCrgAuCDQEvgzJhl52uaYhCg7koQIkYWGa1ZOAr6utf6wUsojyceoJTbFTMVa1TcPI2PG6hzgnEBL4EFMMvKY3QEJUS4kCREiAw3XrHRorT8G+ltKOeok+RizxOG5c7AqIc4qZ7ElIVFnAmcGWgKPAF9ZvXz1v22OR4iS57A7ACGK3dwv/ekEPTT4slLqZ0oVZNTGeJBYCZkPdLsnu2scbkexrwp8CvB4oCVwR6AlMNPuYIQoZVIJEWIEDdesnB4ZGviRw+W5EIfk6zk2nIT4l/gVMBfY453lnWtfSFlRmOG97wq0BFYA31u9fHWfzTEJUXLkyCpEgoZrVrrnfvG+L+tIeJ3D5bnQ7njK0M72Fcu2xm37AS8w6JnsKYZOqdmoAr4BvBpoCch7RYgsSRIiRJy5//WnM3V4cK1yur+lHM5Ku+MpU8k6pQLgrnMXa3+QdBqA3wdaAg8HWgKL7A5GiFIhSYgQQMM1K+fN+cIf/qKU4wHldDfYHU+ZS0xCpmCaN3D68zpdeyGcAjwXaAl8N9ASqCjUgyqluhK2L1NK/aSAj6+UUtcqpVqVUmuVUg8rpQ6N+/t7lFKvKqUetrZ/p5R6USl1tVLq60qp0wsVqygu0idEjHtzPn/PZ5TT8x2Hy1Owk8Y4l6xT6gBOHE6fc7IdAeWYE/giZljv8tXLVz9jd0AF8EngOGCR1rpHKXUmcL9S6lCtdR9wBfAJrfXDSqlpwHFa61Lp/yPySJIQMW7NufquKWh9j8NbfYLdsYwziUnIAUCXd5Z3knIopx0B5cnBwBOBlsB3gK+vXr56wI4glFJzgV8Bk4EdwOVa601KqVuBXuAgTMfgy4HlwLHAU1rry6z7nwmEMGvtrLPu35XwMP8FnKK17gHQWj+olHoCuEQpNRM4AZinlLofeDswRSn1AvApTILyZ6313UqppZjp86uAfuA0oAdYgakyVQA/1VrflNMXSdhGmmPEuDTzylsuwuFqkwSk4DTwUnTDv8TvBGYCPRXTK0q9KSYZF/BV4JlAS2BxHh+nUin1QvQL+Hrc334C3Ka1Phy4A/hR3N8mAG8Drgb+BPwQOBQIKKUWK6XqgWuB07XWRwDPAp+Lf2CllB+o0lqvS4jpWeBQrfXXrZ8v0Vp/ETgXWKe1Xqy1/lfcfjzAncBntNaLgNMxSdIVQIfWeimwFPiIUmreKF8nUWSkEiLGldmfuqNCR8K3uWqnXiQTjtliQ/uKZfFX0fWY/iART72ta8bk2+HA04GWwHXAt1YvXz2U4/33aq2Hkxyl1GXAUdbmsZgp6AF+A3w37nPgTFYAACAASURBVH5/0lprpdRqYJvWerV1/5cxnW1nYRb3e9z6vHiATCdpU5ikM1MLga1a62cAtNadVixnAocrpaKjj2oxKy5vyGLfokhJJUSMGzM+/PPDcLrWumomSQJin2SdUgFw1brKsRISz41p1ng80BKYbWMc8YlBv/U9EvdzdNuFSSQesqoWi7XWh2itr9hnZyZZ6FZKHZDwOEcAr2QR10hJiwI+FRfDPK31g1nsVxQxSULEuDDjip9+3F03/Vmnt3qO3bGMc4lJyPToD86aop2uPdeOBp4PtAROK9DjPQFcbP18CZDN2jdPAscrpRYAKKV8SqkDk9zueuBHSqlK63anY/qB/DaLx1oDzLD6hWAtDOkCHgA+rpRyW78/UClVlcV+RRGT5hhR1qZcGPS4J836X8/khvPtjkUA+ychC4Beh8/hcVSMqynx64EHAi2BrwErVi9fnU2zRbY+DfxKKfVFrI6pmd5Ra73Datr5nVIqOnrsWmBtwk1/jOlfslopFQbeBN6lte7N4rEGlFLvBX5sJTO9mH4hN2Oahp5XpoS5Azgv0/2K4qa0zud7Xwj7TLvkOwvdE2f9xVlVJ53Yisch7SuWvRrd8C/xXw9Eqg6qmlR/Vv0VKe5Xzu4Dlq9evrrT7kCEKDRpjhFlacp7ms/yTJ3/rCQgRaWfuCto/xK/F5gE9HqmlnWn1HTOw4yeOTTtLYUoM5KEiLLia2xyTD7vy5+unLvojw5PZbXd8Yh9vNK+Ylk4bnsKVkdE90R3uXdKTedA4KlAS+C9dgciRCFJEiLKhq+xyV116Kk3+BqP+YFyeTx2xyP2M+KaMa5a13iuhERVAf8baAl81e5AhCgU6ZgqyoKvsamyetFZt1QecNTFyuGQ8bfFKTEJmY0ZCoqzquTXjMml66whvJ9cvXx1OO2thShhUgkRJc/X2OT3Lz3/j74FR79PEpCilmxkTLe73l3jcDtkxeJ9fQy4L9AS8NkdiBD5JEmIKGlVB50wufa4i//unRM4w+5YRFrDSYh/iV9h1ivp9s7yShUkuXOAvwVaAhPsDkSIfJEkRJSsmiVnz6s94ZJ/VUw/8Kj0txY229W+Ytkbcdt+oBIY9EwZ1yNj0jkWeDTQEphhdyBC5IMkIaIk1R570WJ/04WPeurnLLQ7FpGRZJ1SIwDuOrckIakdhpnqfYHdgQiRa5KEiJJTd+IHTq458p0PueumzbI7FpGxFxO2pwBOAKdfOqVmoAH4Z6AlMN/uQITIJUlCRMnwNTapmsVnn1F9+Jl3u6on1tsdj8hKYiXkAKAfJw6nzznZjoBK0Azg74GWgKx/JMqGJCGiJPgam5Ryed7pP/r8X7tqJkkCUnqSJSFd3pneicqhnHYEVKLmYhKR6WlvKUQJkCREFD1fY5MCzvE3XfgD98SZM+2OR2RNAy9FN/xL/E5gFtBTMaNC+oNkbwEmEZEKkih5koSIUnCi/6jzvlUxbYG0h5em9vYVy7riticBCoi4J4376dpH62DgIRm+K0qdJCGiqPkamxZVB06/3jv38MPsjkWM2ojTtcvImDFZBDwQaAn47Q5EiNGSJEQULV9jU2Nl4zE/rGw8dqndsYgxSUxChvszOGuckoSMzVJgZaAl4LU7ECFGQ5IQUZR8jU0zvXMO/171YaefpJSSqdhLW7Lp2nsdPofHUeGosyOgMnMCcIvdQQgxGpKEiKLja2ya5Jm24Ds1Ryw7SzkcMnKi9CXOETIP6K6cUzlF8suceX+gJfA1u4MQIluShIii4mtsqnFNnBnyH33B+crp9tgdjxizfqA1uuFf4vdiOqb2eqZ6pFNqboUCLYEL7Q5CiGxIEiKKhq+xyevw1X6h9piLPuBwe2X10PLwavuKZUNx21MwQ3ZxT5ROqTmmgJZAS+BIuwMRIlOShIii4GtscgEf9i89/4POyppau+MROZPYH2S4+uHyu6QSkns+4H5Z8E6UCklChO2sycjeX3XoqZd46uc02B2PyKnEJGQOViXEWS0jY/JkBiYRqbQ7ECHSkSREFIMT3fVzL/QdeNxRdgcici4xCZkPdLnr3TUOt0NOkvlzJPBru4MQIh1JQoStfI1Ns5S74nL/0RccqxxOl93xiJwbTkL8S/wKsxpst3eWV5pi8u+9gZbAR+0OQohUJAkRtvE1NnmBj/ubLlzqrKyRRenKz672Fctej9v2A5XAoGeyR5piCuOHgZbAwXYHIcRIJAkRtrD6gVxU2XjMsRVT5x9qdzwiL5J1So0AuCZIp9QC8QH/G2gJVNgdiBDJSBIi7HKEq3bqedWHnnqc3YGIvEm2ZowTwFXjkkpI4RwOXG93EEIkI0mIKDhfY9NkHM6P1h570THK6ZYrtPKVmITMA/pxoJw+pzS/FdanAi2Bc+wOQohEkoSIgvI1NrmBj/mPOu9oZ9WE6WnvIEpZspEx3d5Z3knKqaQTcuH9OtASkM+cKCqShIhCe6d37qKTKmYdstjuQEReaeCl6IZ/id8JzAS6K2ZUSFOMPeqB3wRaArJgjygakoSIgvE1Nh2iKqourF501rGycFnZ29i+YtneuO1JmONNxD3JLZ1S7XMa8DG7gxAiSpIQURC+xqY64Er/kece7HBXVNsdj8i7ZJ1SAXDXyZoxNvt2oCUg/wNRFCQJEXlnDce9zDN1wUzPtAWL7I5HFMSLCdvToj84q51SCbFXHXCD3UEIAZKEiMI4AqWW1BzxjiYl7TDjRWIlpBHodfgcHofXMcGOgMQ+Lg60BM60OwghJAkReeVrbKoCllcHzpjh9NXNtDseUTCJSUgD0O2d7Z0seWjR+LkscifsJkmIyLdzHL66SZXzjjzB7kBEwQwAa6Mb/iV+L2ZkRm/FNBkZU0QOAK61OwgxvkkSIvLG19g0BzjLf+Q7D1Iut9fueETBvNq+YtlQ3PbwdO3uidIptch8MdASOMTuIMT4JUmIyAtfY5MT+KB78jyve3LDErvjEQWVbM0YB4DLL2vGFBk3cKPdQYjxS5IQkS9HA401i89aKp1Rx53EJGQ2ViXEWe2USkjxOTHQEniX3UGI8UmSEJFzvsamSuB9lfOXVrn8k+fbHY8ouMThufOBbvckd7XD7ZCOkMXpm4GWgJwPRMHJ+g0iH07H4aypOujEk+0ORNhiuBLiX+JXmIXr9nhne+cUKoAtt2xh7wt7cfldNH6zEYBNP9vEwNYBAMI9YZw+Jwu+sWC/+771wFvs/uduUOCd5WXmFTNxeBxsvnEzfVv6qFlcw7QLzbQn2/+4He9sL/4j/IV6avlyKHAp0GJ3IGJ8kcxX5JSvsakeeFd14PSpDm+1rJQ6/uxuX7Hs9bjtGqASGPRM9hSsP8iEEybQ8PmGfX435xNzWPCNBSz4xgL8R/nxH7V/4jC4e5CdD+1kfvN8Gr/ZiI5oOp7qoG9zHwCN1zXSs7aHcE+YwT2D9K7vLYcEJCoUaAl47A5CjC+ShIhcOw/lwDvn8GPtDkTYItl07RrANcFVsP4gVQurcFY5k/5Na03HMx3UNtUm/3tEExmIoMMaPaBxTXCBE/SgRkc0ekiDA7bfu50pF5RVP9u5wJV2ByHGF0lCRM74GpvmASdUHXziBIenss7ueIQtkiUhZmRMTeGSkFR61vbg8ruomFax39/cE9zUn1XP2s+vZc1n1+CodFBzWA3eGV7cE92sC66jdmktA9tMs07l3LLr4vLVQEtA1nYSBSN9QkQuvRvo8c5dItNBj1+JScg8oB8HyulzFkXzXMeTHdQ1Jc+Rw91h9q7ay4HXH4jT52TTTzex54k91B1Xx/RLpg/fbuMPNzLjshlsv387fZv7qD60momnTCzUU8inKcDVwDfsDkSMD1IJETnha2yaDRxWecBR1U6ff3raO4hylZiEzAe6vbO8k5RT2X7Ro8OajudGborperkLd70bl9+Fcin8R/npaevZ5zadz3dSOa+SSH+E/tf7mfPJOex5Yg+R/kghnkIhfCHQEiiLjEoUP0lCRK68HRionL/0OLsDEbbR7DsyxgnMBLorplcUReeJrpe7qJhegXuiO+nf3ZPc9K7rJdIfQWtN9yvdVEyPNdvoIc3Oh3ZSf3Y9kYEIRGfA0eZvZcKP9A0RBSJJiBgza0TMcZ7pjRGZF2Rc29i+YtneuO1JmGNMxF1f2OnaN/98M+uvW0//m/2suXoNu/65C4COp/ZvihncPUj7D9oB8M334V/qpy3YRtu1beiIZsIpsUV/d/59J3XH1+GocOCd7QUNrde24mv0jdgRtkRdJSNlRCHYXh4VZeEUQFctPFFGxIxvyaZrB8Bd6y5oJWT2x2cn/f2sj8za73fuCW4aPtcwvD31/KlMPT95zlT/9li3FqXUiI9TBqYDFwO32R2IKG9SCRFj4mtsqgbOcNVN63ZNnHGY3fEIWyUmIdOxGiycNTJdewm62u4ARPmTJESM1bGAu+qQU49SyiHvp/EtMQlZAPQ4fA6Pw+uYkOwOoqgtDrQETrU7CFHe5KQhRs3X2OQBznV4azo8U+YdaXc8wnbJhud2e2d7J8sahiXrc3YHIMqbJCFiLI4EqqsPOy2gnC7pxDa+DQCvRTf8S/wVQD3QVzG1QppiSteyQEvgQLuDEOVLkhAxKr7GJifwLhzO3Z4ZC5vsjkfYbk37imVDcdtTMEN2tXtiYTulipxSwGftDkKUL0lCxGgdAkyrPODIyQ53hUzzLF5M2J6K1SnVVVsc07WLUbs00BLw2R2EKE+ShIis+RqbFHAusLdi5iEyIkbA/v1BZgERAGe1Uyohpa0aOM/uIER5kiREjMYMYL5yuve4J0w/yO5gRFFINjKm2z3JXe1wO+QquvR9wO4ARHmSJESMxhJAV85fOl853V67gxFFIX66dgU0AF3e2V5piikPZwZaAvK/FDknSYjIitUUcwqws2LGQdIUIwD2tK9YtiVuuwbwAYOeyR5piikPTuB9dgchyo8kISJbs4GJyl0x4KqbttDuYERRSGyKmYrVH8Q1QTqllpFL7Q5AlB9JQkS2jgAilfOPbpS5QYQl2ZoxDgBXjUsqIeXjiEBL4GC7gxDlRZIQkTFfY5MDOAnYWTFjoTTFiKjE4bkHAAM4UE6fc7IdAYm8kWqIyClJQkQ25gJ1yuMbctVObbQ7GFE0EishBwDd3pneicqpZKXu8nKJ3QGI8iJJiMjGkUDYt+DohcrhdNsdjCgaL0V/8C/xOzFzhHRXzJDp2svQnEBLYIndQYjyIUmIyIg1TftJwE7P9AMPtTseUTQ2tq9Y1hm3PQlzXIm4692ShJSnc+wOQJQPSUJEpuYB1Q5vjXb5p0hTjIhK1ikVAHetrBlTpiQJETkjSYjI1JFA2Nuw+ADlcDjtDkYUjcQkZDrWmjHOGqdUQsrTUpm4TOSKJCEiLV9jkws4EXjLPWnWHLvjEUUlMQmZD/Q6Kh1uh9cxwY6ARO7piNbh3vBLwFcxFyTbbQ5JlAnpuS4yMQ8zA+ZbLv/k2XYHI4pKspExXd453ilKKTviETkSGYh0DewYaOvb1Nfa9VLXW+Hu8LbOVZ3fsjsuUV4kCRGZmA9o5fa6HJX+6XYHI4rGALAmuuFf4q8A6oHNFVMrpD9IidERHRnqHNrcv7W/rae1p7V3fe82zDliAuYiZLJ/id/VuapzyN5IRTmRJERkYhGwt2LWIbOUckgTnoha075iWfwJaQqgAe2eKCNjSkGkP7J3uNrxStf6cFe4H6gG6jBLNIQxk9E9C7RKAiJyTZIQkZLVH2QB8Kanfm7A7nhEUUm2ZgwArlpZM6YYxVU7Wntae9oSqh3TrJttBf4MvAy0d67qHBxxh82104CzgLOBe2nuuDOvT0CUHUlCRDozMB2Yw67aqdIpVcRLTEJmYSohOKud0hxTJCL9kc6BHQNtvRt7W7tf6d4Q7t6n2jEHGMT8L58B2jpXde4ccWfNtS7gWEzScTamShrt/KMBSUJEViQJEenMITrksnrCLJtjEcUlMQlZAHS7J7mrHW6Hz46AhFXt6Bja1L+1v7VnbU9bb3vvdvavdrwB3A+8Svpqxwxi1Y7TMclLMqfTXOuguSOSo6cixgFJQkQ6hwG9nmmNU5TT7bU7GFFUhpMQ/xK/wqwttNc7yyvJaoFF+iIdAzsG2no39bZ1vdy1PtITGQBqiFU7Boj17WjrXNW5a8SdmWrHcexb7cjEJMwq28+O+omIcUeSEDEiX2OTAg4FOjxT5x9udzyiqOxpX7Fsc9x2DVAF7PRM8Uh/kDzTER0e2mOqHd1ru9v6NvbtwBzPJ7Jv3477MNWOjWmqHTOJJR2nA/5RhnYSkoSILEgSIlKpxzqxuCfMkPlBRLxk07VrAFedS/qD5EG4L9wxuGOwtXdjb1vXK10bEqodszF9O14AnsNUO3aPuLPmWjdwPLHEI1edzo/J0X7EOCFJiEhlOPFw1kySTqkiXrKRMQrA5ZeRMblgVTs29m/tb+t+rbu1b1PfW4Ab07djOibpex14mFi1Y+QhtM21s9i32lGTh7CPzcM+RRmTJESkshAYcvqnVDs8lSN1RhPjU2ISMg8YwIFy+pyT7QioHIT7wnsGtg+09m3sM9WO3sgg+1c7VgHPY+bt2DPizpprPcAJxBKPQqx+PYvm2pk0d7xegMcSZUCSkCwopaYBNwBLgX6gHfis1nqtnXHlUQDo8EyZJ7OkikTJ1ozp9s70TlROJceVDOmIDg/tHmrv29rX1vNaT2vf5r6dmGrHREy1A2AL8HfM7LSb0lQ75hBLOk7DDMUttGOBu214XFGC5GCRIWUWwvgD0KK1vtj63WJMGbokkhCllEtrndGMh77GpmpMB7dNrpr6ifmNTJSgl6I/+Jf4nZg5QrZWzKiQvkNphHvDu+OqHe2RvsgQsWqHDzOS5XlMxaMtg2rHScSG0B6S7/gzcAyShIgMSRKSuVOBQa31jdFfaK1fUMb1mAOABq7TWt+plDoFaAbewgxzfQ74gNZaK6VWAOcCQ8CDWusvKKVuBf6stb4bQCnVpbWutvYTArYBi4F7MVehnwEqgfO01uuUUpOBGzHD8cBUaB5XSjVjJhxrsGJ5f4bPd6b1fHBU1U3K5oUSZW9T+4plHXHbEzET2kXc9W7plJpAh/XQ4J7B9v43TN+O/i39u9i/2rEJ+Bumb8emzlWd4RF32FzbQKza8TZM5/FiIv1CRMYkCclcNJFIdAEmOViEGU3yjFLqUetvSzDtsG8AjwPHK6VeAc4HDrISkkz6WiwCDgZ2AeuBm7XWRyulPgN8Cvgs8D/AD7XWjyml5gAPWPcBs/T2CVrr3iye7yTMiQVnpV8qISLeiNO1u2tlzRiAcG9418D2gbbe9t7W7le62yP9kTCm2lGLSRr6MceTaLWjY8SdNddWYKod0cTjoHzHP0ZH0lzrorlD1pkRaUkSMnYnAL/TWoeBbUqpf2L6jHQCT2uttwAopV7AVCOeBPqAm5VSKzFrNKTzjNZ6q7WfdcCD1u9XYyo0YHq7HxK3fLpfKRXt/X5/lgkImErIIICjokoqISLeiwnb04gmrDXjc7p2HdZDg7sHN1jVjrb+1/t3AR5MtWMGZuRQO/AQptqxOU214wBMwnEW5jNebNWOVCows+euSXdDISQJydzLwIVJfq+S/C6qP+7nMODSWg8ppY7GdBq7GLgKU1IdwjqQW/1PPCPsJxK3HSH2P3QAxyYmG1ZS0p0ixpHMAnpxOB3K460dxf1F+Uo2XXuPo9LhdngdE+wIyA7hnvDOaLWj65WujXpAhzGTfEWrHX2Yibuex1Q7OkfcWXOtFziZWLXjwHzHn2cHIUmIyIAkIZn7B/AtpdRHtNa/BFBKLQV2A+9VSrVgrnpOAr7ICCVTpVQ14NNa/59S6kmgzfpTO6bZ5C7gXZg242w8iElorrceZ7HW+oUs9xFvFtDrnjirTimHYwz7EeUn2fDcLu8c7xQVV4orNzqsBwd3D7b3v9Hf2r2mu63/jf7d7FvtANgA/BVzAt6Sptoxn1jScQqmU2q5OBgzW6sQKUkSkiGr/8b5wA1KqWswVzntmP4Y1cB/MB05v6S1flMpNVK7bQ3wR6WUF1NFudr6/S+t3z+NGY6XbfXi08BPlVIvYv6vjwJXZrkPAHyNTdEJkTa7/PUyPFfEGwRei274l/grgMnA5oqpFWXXFBPuCb81sC2u2jGoI8SqHTVAL/A0sb4de0fcWXNtJSbZiDazNOY5fDsVe78VUSSU1truGESR8TU2TQW+BWyuOuy0RVULjz/P7phE0VjdvmLZ8DpC/iX+2UAQ2DLlvClnVTZUNtkX2tjpsB4c3DW4of+N/tauV7vaBt4c2EOs2hFtIt0APIVJxjZ3ruocedXY5tpGYtWOkzEj2saDZ2juONruIETxk0qISKYOa3ius9I/2oWs8m7Lzz+Ew1MJDgfK4WT68hvoXvMYHY/9lsGdm5n2wR9QMT35xWay+wLsfuTX9K5/Ds+UedSf83kAul76B5G+vfiPelfBnlsRS7ZmjAPAVVuaa8aEu8M7rL4dbUmqHX5MVfIpTLVjXQbVjlOJJR7z8x1/kVpodwCiNEgSIpLxY51YHN7qok1CAKa+71s4fbF+s576uUw+/yvsfOAnWd830t9N/+uvMuNDP2HHn65nYEc7rrrpdL/0N6a85+t5ib8EJSYhszEdpHFWOUtieK4O64HBXYMb+l7va+1e09028OZAB2ZEx0TMqDAwQ+FXYiYi3JKm2rGQWNJxEuDNZ/wlwi/Tt4tMSBIikhmeu8RR4SvqJCSRu34sE3YqdHgIrTV6aADlcNL59L3UHHkuyikfFUvS6drdE91VDo+jaDtWhrvDO/q39bf2buht617TvcmqdtTGfXUDT2BWoV3Xuaqza8SdNdf6MCPaoonHvHzHX6IaMQvsCTEiObKKZKZipo5GeSqLNwlRiu13/TcA1YvPpmbxWWO6r6PCh2/hcWy99dN45y5CVVQxsHUtdce/Lx/Rl6rhOUL8S/wKM/fNXu9s7yzbIkpCD+mBwV2D6/te72vrfrW7dWD7QCf7Vjs0ptrxJ0y14/U01Y6D2LfaUZHnp1AOZqS/iRjvJAkRyUzBmotEOd1F25Fu2iXfxVUziXD3HrbdeS3uSbPwzj5sTPetbbqQ2iYzHczOv/yIuhM/wN7/PEDfhlW4pzRQd9zF+XxKxW5P+4plm+O2azDzYez0TPHY3hQz1DW0fWD7QGvveqvaMaQ1pspRZ311AY9hEqm2zlWdI49Aa66twszlEx3J0pDn8MvRNLsDEMVPkhCRTD3RCdGUw2lvKCNz1ZiJXJ1VdfgOPJb+N9ZmnISku+/AtnXmdhNmsutvv2DaJd9hxx+/w+Cu13FPnJl0n+PASwnbU7A6MLvqCt8pVQ/p/sFdg+v7tvS1da/pbourdkzCzHOjMfPw3I+pdryRptpxCLFqx4nsO2GgyJ4M7xdpSRIikpkEbAdQylGU75HIQB/oCI4KH5GBPvo2rKI2w2aTTO6751+3M/HtV0FkCLR13lIO9FB/kj2OG8nWjFEALr+rIJWQoa6hbQPbBqJ9OzbrIQ37VzsexVQ71qWpdlQTq3acTWzxR5EbkoSItIryBCPs42tsUpirSTPTo0MVZSUk3LOHHfdeZzYiEaoOOZnKA46kZ+0T7HroJsK9HWy/O4RnyjymvvcbDO3dyc6//oip7wmNeN+onrX/xjOtcbhaUjHjIN645ZO4pzTgmXJAoZ9qMUlMQhqAQRTK6XNOzscD6iHdP7BzYF3/6/1tXa90tQ2+NbgXM/pkIrFqRyvwR8y8HVvTVDsOI5Z0nED2MxOLzEkSItKSycrEPnyNTU7gZmAjwOQLrv2aTNsuLCe2r1j2WHTDv8QfBPzeWV7P1AunXpWrBxnqGnpz4M2Btp4NPa3da7q3WOlwdIZSMItDPkOs2tEz4s6aa2swiztG+3aMZfiUyM4rNHccancQorhJJUQkcmK18wNIAiLiDFdC/Ev8Dswok20VMyrGNDImMhTpG9w5uK5vS19b9yvdbYM7B7sw1Y74vh2vYRKPaLVj5Kun5trDiSUdxyPVDrtIJUSkJUmISDT8nlAuT1E2xQhbbGpfsawjbnsSJmENuye7s+oPorUm3BXeOrBtoK1nXU9r92vdW4igMH06JlpfHZhFI1djqh29I+6wudYPnEEs8Ri3PYeLzASaax00d4zcPCbGPUlCRKLhxEOSEBEnWadUDeCuTZ+ERAaHqx2t3a90tw3uGuzGrKMykdisq69hFoNbC7yZptqxiFjfjuOQY1mxqiT7xTjFOCIfXJFouDlGOd2ShIioxCRkGlbC6qxx7jc816p2vNH/Zn9b77re1u613a/HVTsmWV97MCtGrwbWp6l21BGrdrwdmQirVEgSIlKSJEQkiq+EyPtDRCUmIQuAHofX4XZ4HRMAIoOR3sGdg+v6Nve1dr3StW5o91C02jGBWN+ONcSqHdtGrHY01ypgMbFqxzHI8aoUFe1U/qI4yIdaJIpVP6QSImI2JWzPA7pddS5fT1vPo73retu6X+t+HT1c7ajHVDt2s2+1o2/ER2iuncC+fTtkxs3SV7QzLoviIEmISBTXHOOSJERE7Yz+4F/irwAmA5sH3hzoeWvlW08Tq3ZEgFcxI1laSV/tOIJYtaOJ+CRYlAOphIiUJAkRiWLNMZKEiJi34n6ejJnQbg4mYd0FPISpdmxIU+2YCJxJrG+H7WvOiLySSohISZIQkSj2ntDITHYCTHVjV9x2D2Zq9Jcx1Y7taaodRxKrdhyNVDvGE6mEiJQkCRGJhk8Q4d4UoxXEeLKnfcWycHSjc1XnLuCmEW/dXFsJnE+s2pGXKd1FSVB2ByCKmyQhItFwEhLp3i1JiIB9m2IycTRwRz4CESVnwO4ARHGTKblFosHoDzo8GNbhITmIiIySkHMXuuvPXeg+5u5XBi/Nd0Cicf9qXQAAIABJREFUZMjxQ6QklRCRaJ/qhw4P9iiny2NXMKIopE1Czl3obgCuBRzKDN8VAiQJEWlIJUQk6iGuHVcPDYy8QqkYLzKphEzEvG821fuUrBUioiQJESlJEiIS9RD3vtBDA9IvRGSShPiwktdqj5IRESJKkhCRkiQhYh89rU8NAf1YHVT1YL9UQsTO9DfBjzXJXZVHhmWKYZKEiJQkCRHJ7AXcAJHBPklCRCaVkAlYnZp9bqmEiGGShIiUJAkRyXRiJSFakhCRWRJSi5WEVLqkEiKG7bY7AFHcJAkRyXQQrYQM9EoSIrJKQrwuqYQIAHpo7pDjh0hJkhCRzHASovt7pGOqyCoJqZBKiDB22B2AKH6ShIhk9hCthPR3yZWMyCQJqQEGvS6cHqeSeWUEwHa7AxDFT5IQkcwerNEx4e49XTbHIuwVJk27/rkL3U7MEN2hadXSFCOGSSVEpCVJiEimB7NyKgNvbdypI5FwmtuL8rWrfcWydKspV2K9X6ZUOSQJEVGShIi0JAkRycT6gYSHIpH+7mwXMBPlI9OJygCYWCmVEDFMmmNEWpKEiGQ6sCaeAoj0dGyzMRZhr0yTEA0wwStJiBgmSYhIS5IQkcx2zHtDAQx17ZQkZPzKZLbU4cSj1isjY8Sw9XYHIIqfJCFiPz2tT/Vj2nMrAYb2bJUkZPzKat2YGlk3RsS02h2AKH6ShIiRrAeqAAa2t0sSMn5lmoQ4QBavE8M00GZ3EKL4SRIiRtKGVQkJd27v0kMDMl/I+JRJEuLHGh0ji9cJy+s0d8hEhyItSULESLYS1zk13LtXOpmNT5kkIXUMrxujKvMbjigR0hQjMiJJiBjJNqx2foBw925pkhmfsktC3FIJEYAkISJDkoSIkezGnFhcAOHOHZKEjE+yeJ0YDUlCREYkCRFJ9bQ+FQE2YnVOHdz9uiQh41OmfUKsJEQqIQKA1+wOQJQGSUJEKuuIjpDZtn671jrd9N2i/GSchFR7cLkcyp3vgERJWGV3AKI0SBIiUmnHao7Rg31Dkf4uWQtifBlsX7GsI9UNzl3odmFGUQ1Nq5Z1YwQA22nu2GJ3EKI0SBIiUtlG3AiZoY7tG2yMRRTergxuM7x43WSf9AcRADxvdwCidEgSIlLZTtwImcHt62Ua5vEl04nKIiCL14lhz9odgCgdkoSIEfW0PtWDqYZUAfRufLFd60jE3qhEAWW1gm6dLF4njKfsDkCUDklCRDrPAhMAdH/3QKR7j7T1jh9ZrRsji9cJy5N2ByBKhyQhIp1XiG+S2b1VmmTGj6ySEFk3RgDrae7I5H0jBCBJiEiv3fruABh4c+06+0IRBSZJiMjWv+wOQJQWSUJESj2tT/ViFrPzA/Rtfvl1Wcxu3Mh0ttQwQJVM2S7gIbsDEKVFkhCRiWewkhB0RA92bJMpmceHTJKQCQyvGyOVkHFOI0mIyJIkISITbcTNFzLwZptMyTw+ZLVuTKVM2T7evUhzh6y2LbIiSYjIxGagB6gA6N3w/DodiYTtDUkUwM4MbiOL14moB+0OQJQeSUJEWj2tT4UxY/8ngRmqG+7aKbOnlr+sFq+rcFGZ33BEkZOmGJE1SUJEplZhrSMDMLCjXZpkyl/GSUhtBR6XQ7nS3lqUqz5kZIwYBUlCRKbWYUZBOAF61z39qsyeWtb621cs25vqBucudLsBDxCWxevGvUdp7uizOwhReiQJERnpaX2qD3gRa/bU8N6d3UN73lxjb1QijzLpDzK8eF29T0lTzPj2B7sDEKVJkhCRjaew1pEB6Nv4n+dsjEXkV6YTlWmQxevGuTBwj91BiNIkSYjIxsvAEFbfkN51z6yP9PfstjckkSeyeJ3I1CM0d+ywOwhRmiQJERnraX2qG3gcmBL93cCbbc/bF5HIo6ymbPdXSBIyjt1ldwCidEkSIrL1KOCObnS/9tgq6aBalrJKQmoqZKKy8UhrPQTca3cconRJEiKytQF4A2sa9/Det7qH9myT4brlRxavE2kppR6WVXPFWEgSIrLS0/qUBv6KNUoGoG/jC8/aF5HIk0xGx0zA9BHCJ+vGjFfSFCPGRJIQMRrPIx1Uy10mV7d1WLOl+spgBd2+Ic3Rv+xi0Y1dHPqzLoIPm2kvNuyO0HRzF40/7uK9d/cwENZJ7//itjDH3tLNoT/rIvDzLvqGNP1DmrNu7+awn3Xxs2cGhm/70T/1smpraa98oLXuRUbFiDGSJERkLa6D6uTo7wa2SQfVMpPV4nXlsG5MhRP+sbyK/1xZzQsfq+Kv64Z4cssQ//W3Pq4+poLWT1Uzwau45fnB/e47FNF84N5eblzm5eVPVPPIch9uBzywbogjpzt58eNV/OI5k4T8580wEQ1LpjsL/RRzSil1F80dcvEhxkSSEDFaj2JmywSge410UC0zWSYhpV8JUUpR7VEADEZgMGw6vPxjQ5gLDzEz0i9f5Oa+1/ZPQh5cN8ThU50smmYSi0k+B06Hwu2A3iEYivtkfO3hfr5+akXen08B3Gh3AKL0SRIiRivaQbUGpINqGcpu8Tpn6SchAOGIZvGNXUy5fi9nHOBi/kQHdV5wOUxyMsvv4PXO/Ztj1u6MoBS8/fZujripi+8+3g/AGfNdvNkVoenmbr50fAX3vzbIkdOdzKgp+UPvf2jueNLuIETpK/lPgrCH1UH1AWBi9He96599yr6IRI6lTELOXehWmAR0cGKlqnA6VFkcS5wOxQtXVrPlczU8/UaYV3fsX9xTav/7DUXgsU1D3HFBJY99qIo/rBni7+uHcDkUv323j1Ufq+Y9h7i44ckBPn+ch8890MeFd/Vwf5KqSom4ye4ARHkoiwOHsM0+HVT72ldtHNq7c4O9IYkc6G1fsawnzW3cmP97ZGpV6fcHSVTnVZwy18WTW8Ls6TN9PgC2dEaYUbN/FjLL7+DkuS7qfQ58bsU7Frh4PqHj6c+eGWD5Ijf/3hzG44Q7L6zkukf7C/J8cklr3QXcbnccojxIEiL+v717j46zvvM7/v7NaHQZyTYG2zIJxgQjvBgSQkhQk80moRuabUhJts1lt9k220Nz2t2zPafbs2RbkrRO2M2STZZmaRIghC5QDpeE62BMwPcLmPH9Knk8vsj4ItmydRvpkTTPM8+vfzwjoxjZ1hhJz1w+r3Pm2Ho0M3xlbOlzvr/n9/teNCed7AfeZNQNqgOta1aEV5FMkILmxswukxDSOeDTMxSEjUHXsvyQx3WzI9z6gSjPtngAPLbD5YsLY+967ecWVLHzRA7HtXi+Zc1hj0Wz3/n22j1oWZL2+Pc3xnBcS8QEHZUhb2q+tolkjHmSxb3nnbAsMl5VYRcgJW8F8CmCQOsPH9l9zL32d1OxSxoXhlyXXLyCQsjMMpkb095v+caLDjkffAtfvT7GF66NsWh2lD961uE7K4e46fIod94UhJBEymXz8Rzfv7WWmXWG//bxaj728AAG+HxTFbdf+05Y+f6aYb7zezUYY/jcNVX8bFOWDz4wwH++ufoc1RS1n4ddgJQPY+3Ye95Fxive1PyfgI8A7QDVc5vmzPjEH/2ZGWvxXErBsrZ7b/8X53vCHQtj1wD/HTj6jRtjN/6bRbEvTU1pErJXWdz7+bCLkPKh5RiZCAmC7bpRgGxH+qTXfXx3uCXJezCe01I1vK4y/W3YBUh5UQiR98xJJ9uBNcDckWv9u5av0rkhJUvD6+RdfGvXs7j3jbDrkPKiECIT5RWCv09VAO6pw13uqSPbwy1JLtJ4Qkg9+RBSr7kxFSFijLogMuEUQmRCOOlkJ7CM0d2Qna+vsb5f2gMyKtN4T0v1AOo1Qbfs+dZuY3Hvb8KuQ8qPQohMpN8Q7JiIAXg97X3Zkwc1Ybf0jCeEzCR/WmpdFXWTW46ELWLMD8KuQcqTQohMGCed7CFYlhnVDXltnfW9kj0WskJV3PA6OTff2lbg+bDrkPKkECITbQXBD6cagFzm9EC2fb9mTJSWihteJ+cWMeZbLO7VTeYyKRRCZEI56WQGeBFoHLmW2b50vZ8d6guvKinQuIfXGaBGyzFly/PtWhb3Lgm7DilfCiEyGdYADgQ/nPyh/uxA65qXwy1JCjDu4XWz601txJTH8Dr5bdZaWxUxfxl2HVLe9M1DJpyTTg4SrCGf6YYM7k/uz556W1t2i99A2723X2iq2sjBdP6cMpkbI+/m+fyKxb1bw65DyptCiEyWdcARYNbIhb6Nz7/mu8P94ZUk4zDeg8p8gFlxhZBy5FubjUXNX4ddh5Q/hRCZFE466QK/JDjUqgrAH+wbcvau0/pycStoeN2ldQoh5ci33M/i3sNh1yHlTyFEJo2TTh4GXgLef+bavjdTbtcxzZUpXuMNIQDM0NyYsuP59nRVxPxN2HVIZVAIkcm2FOgALh250Lfx+aW+lx0IryQ5j4Lmxmh4Xfkx8Bcs7u0Nuw6pDAohMqmcdDILPEywpbMKIDfQPejse3NpqIXJuRQUQhqqdUZIORnI2lXR7/c9HXYdUjkUQmTSOenkQWAJo5dlWte2uN3treFVJedQ2PA6zY0pG55vh2NR/jTsOqSyKITIVFkCnCSYOQJA36YXXrFedjC8kmQMBc2N0QTd8uG4fK/6nr63w65DKotCiEwJJ50cItgtM4PgjAlymVMDzv6Nr4ZamJxtPCHkEkaG18W0HFMOBrK2dXqN+WHYdUjlUQiRKeOkk2mCSbtnlmUG9qzc5XYd3RVeVXIWDa+rML61fizK1zUfRsKgECJT7SWgi+AHGQA9bzz1cm4wcyK8kmSU0+N4jobXlZHeIf6h+p6+bWHXIZVJIUSmVP5I918SbNmtArDZQbcv+ewz1nOHQi1OoIDhdRGDqY5SO9kFyeTpGbK7Z9aZ/xF2HVK5FEJkyjnp5F6CSbvzRq65p49097eset5aG15hAuMbXtcAuI31pi5ijJmasmSiDXt2qD9rv8ji3lzYtUjlUgiRsCSAHcD7Ri4Mpt9KDx9rWR1aRdLXdu/t7gWeU0OwPdc2Nuh+kFJ2tM/+1yvuyxwMuw6pbAohEgonncwRLMtkGL1tN/ncGrenIxVaYZWt0LkxdZNbjkyW4xl/6YL7Mw+FXYeIQoiExkkn+4D7Cdr7Z+4t6Fn3xHO5wb6O0AqrXAWFkJm16oSUor5heyLn89Ww6xABhRAJWX7I3SMEyzIRAJt13N43n37Kd4f7Qy2u8hQ0vO4ShZCS4+as157xvzzvf2c0u0mKgkKIFIMNwKvA/JELXk9HX2bry09ZP+eFV1bFKWhuzDQNrys5+077dy/8af/6sOsQGaEQIqFz0kkL/BrYBlwxcn34aMvxgb3rXtCOmSkz3hASAZimuTElJXUq9/L1P+//Udh1iIymECJFwUknPYJpux3AnDPXW9e2DB3e/npohVWW8YSQBvL3hNRrgm7JONrn739xr6f7QKToKIRI0XDSyQHgHwGfUSeqZra8vGHw8I7loRVWOcZzWuqZ4XVxDa8rCV2Dtnt1m3fbXy8f0mGAUnQUQqSoOOlkJ/ATghByZgtoZvNLbyiITLrChtfpyPaiN+TZ7Jo27yt/8vxgW9i1iIxFIUSKjpNO7gd+CjSiIDKVChpeV6dOSFHzfOuvOOh96w+fcVaEXYvIuSiESFFy0smtKIhMtYJCSE1UnZBi5VtrX9vv3f/QFvf+i3m9MWauMeZpY8wBY0yLMWapMebaia7zIur6kjFmUdh1yMRRCJGi5aSTm1EQmUrjCSHTALcqouF1xey1/d6vHtri3pVIuQVvLTPBPKAXgNXW2gXW2kXA3QT/Di/02mjh1Rb0Hl8CFELKiEKIFDUFkSljucCNqXcsjEWAesCb22Diml1XnFYe8lY+sNm9M5FyL/aMnVsB11r74MgFa+12YL0x5kfGmN3GmF3GmK8BGGM+Y4xZZYx5EthljLnKGLPXGPOYMWanMeZZY4KlO2PM7xtjtuVf/3+NMTX5623GmP9pjFkPfMUY801jzCZjzA5jzHPGmLgx5hPAHcCPjDHbjTEL8o/fGGO2GGPWGWN+5z380UkIFEKk6J0viAwd3qn17onR03bv7ReaplpLfnjdnHrdD1KM3jrqbfrJW9kvJ1LuezkR9QZgyxjX/zXwYeBG4LMEYeDy/OduAb6d75oALAR+Ya39ENAH/LkxphZ4FPiatfaDQBXwZ6Pef8ha+0lr7dPA89baj1lrbwRagTuttW8SDL68y1r7YWvtAeAXwH+x1t4M/BXw8/fwdUsIFEKkJJwriPRtfnG9gsiEKGhuzGV1CiHFZntHruUH67JfSKTc7kn6T3wSeMpam7PWngDWAB/Lf26jtfbQqOcesda+kf/9E/nXLgQOWWv35a8/Bnxq1GueGfX7G/KdjV3A14Hrzy7GGNMAfAL4tTFmO/AQcPnZz5PiphAiJWNUEJnLWUFk8PCO5TpZ9T0pbHidQkhR2X0yt/++DcOfT6TckxPwdnuAm8e4fr71t7M7L2f/Y7QXeP3Z7/Eo8Bf5jsn3YMz7jyJAT74rMvK47gL/DSkyCiFSUs4VRDKbX3pjoHXNr62fc0MrrrSN56CyM8FjhubGFI2t7bnUPWuGP//4DvfwBL3lSqDGGPPNkQvGmI8B3cDXjDFRY8xsgi7GxnO8x5XGmI/nf//HwHpgL3CVMeaa/PV/R9BNGcs0oN0YEyPohIzI5D+HtbYPOGSM+Uq+RmOMubGwL1XCphAiJcdJJzcxRhBxWte29L717CN+drA3tOJKl4bXlaANR7zWe9YMf/mZPW56ot7TBi3FPwRuy2/R3QMsBp4EdgI7CILKt6y1Hed4m1bgG8aYncClwAPW2iHgPxAsn+wiOBn5wXO8/rtAElhGEF5GPA3clb+5dQFBQLnTGLODoIPzxYv8siUkRi1sKVXxpuaPAn8O9OYfAEQbLovP+N0//mpVw6Xzz/liOduP2+69/a7zPeGOhbFPAncCh//Xp2s+d/P7ov9sakqTsaxu83bdtyH7p4mUuzXsWkYzxlwFLLHW3hByKVIC1AmRkpVfmvkBwV32Z84wyPWfdrqWP/h49uShse7wl7GN94wQCxCP6aCyML1+wNt234bs14stgIgUSiFESlr+iPfFBNN3r2Tk5rec5/es+39LnAObXrHW98OrsGQUNDcmHjN1F3iuTAJrLS+n3ORPN2b/bSLl7gq7nrFYa9vUBZHxUgiRkuekk6eBHwIbgA8AsZHP9W9/dXNm6yuPWy/rhFVfiShseJ06IVPO8633T9vd5Q9vdf8kkXL3XvgVIsVPIUTKgpNODgGPAE8BVxCc7AnAUNu2w93rnng4N5g5EVZ9JaCguTG1VboxdSo5rnV+uD770ot7vW8mUu7+sOsRmSgKIVI2nHTSd9LJV4EfA9OBWSOf87qO9nQtf+gRt7u9NbQCi9t4Qsh0zoQQdUKmyinH77p7xdAzyWO5v0yk3Law6xGZSAohUnacdHIXwQFHAwRdEQBs1nG7Vz78K2f/xldszsuGVmBxGncIqY4SqY4GMz9kch3o8o/+1evDDx/stnclUu6RsOsRmWgKIVKWnHTyOHAP0EJwn8iZyZz9O36zuXvNoz/3+joPhFVfkfEJDqI6p9HD6y5v0FLMVNhwxNt717KhH3cN2u8nUu54DpMTKTkKIVK2nHSyH7gfeAWYT/6kRQCv+3hv17IHnnDSbyVszh0Oq8Yi0d127+0X2kFUR7A9V8PrJpmbs9lHt2fX/9367Pc8n58lUq5uqpaypRAiZc1JJz3g1wT3icSAeYz6e9+/8/Vt3av+6Wde78kJO3GyBBU2vC4eUQiZJKcc/9TdK4Zfeb7V+y7wTCLlemHXJDKZqsIuQGSyOemkBXbGm5rvBr4CfIZgVkofgNfbkela/uCT9Tf8/o3xBbf8gamKjTUsq5wVFEIuqdVNqZNha3uu9e/fGH7DcflJIuXuCbsekamgTohUjPzyzKPA3xMcavZbXZGB3St2dK165GduT0cqnApDM94QAmh43URzc9Z9fEd27eLVw884Lt9WAJFKohAiFcVJJ62TTu4BvkMwwXM+wfkXAOT6TvZ3r/jF0wOt656zXnYwrDqnmIbXheTkgH/i2yuHlz7b4j0I/F0i5Z4MuyaRqaTlGKlITjo5ADweb2reBPxHgiPfjwE5gIGWVbuHjuw8NO2mL/zz2KwrbzLGmBDLnWzjDSERgIZqhZD3Kufb3PKDuc0Pbcnu9HweBLYlUq6miUrFUQiRiuakk63xpubvAl8CPkewVbUHIJc5PdCz9rGXqxsXvNXwwc9+tmpG47Vh1jqJxntGiA9QryPb35OTA/7x+zZkky2d/k7ggUTK1Um+UrEUQqTiOemkAzwZb2reQtAVmQ8cJ386aPbEgc6uEweeqr3qpvn11/3ebdH4Je8PsdzJUODcGHVCLobnW2/FwVzywc3ZAznLUuCFRMrVoXlS0RRCRPKcdDKV74r8AXB7/nI7+Q7AUNu2w0Nt234Zv+5Ti+JXf/TWSG3DrHO9V4kpLIToyPaCdfT7R//hzezG1Gl/P/Cw5r+IBBRCREbJD8J7Md7UvBb4VwTbeYeAk+S3qDqta1ucveta66/7zPV1H/jIpyO19aUeRsZzGueZ4XXqhIyf49rMS3u9DU/vdjssLAFeTqTcobDrEikWCiEiY3DSyS7gsXhT8wrgy8BNBOeKBD+wrbUDLat2D7Su3lO/6NYb6q666dOR2vrLwqv4PSlogm5NVJ2QC/F86208lkv+n2T20IDLUeCXiZSrMQEiZ1EIETkPJ508Gm9q/kegCfgqcA2QYXQY2bNy10DL6t31iz59Q+28D94Srb/kinO/Y1EaTwiZBnTFY1TFoiY22QWVsgNdfutPN2a3Huj2XYLux5JEquJHA4iMSSFE5ALyJ67uizc1/y3wOwSdkQX8Vhjx7cCeVbsG9qzaVX35tY3xBbfcHJs170MmGiv2abMe+d1A53LHwliUYHaMd3mDmT4lVZWg047f8cROd92KQ7lBYAfBsevHwq5LpJgphIiMUz6MtMabmv8GuI4gjFwN9BOEEQuQbd93Itu+b6mprltWv/CT19e8/7qPRuuLdkdNV9u9t1/ofIqR4XXMrtfcmLOddvwTS/Z5bzzf6mUsdAKPA7t17ofIhSmEiBQoH0Za4k3N9wCLgH8JXE+wi6aT4EZWbHbQ7d+1bHv/rmXbqy+/tjF+zS03xy4ruu5IQXNjZtaausktp3ScdvwTr6S9Nc+1eBkb/L9/Flitbbci46cQInKR8mFkD7An3tQ8B/g4cBvQCAxQGt2RwkJInXbGnHb8E0vT3tpnW7weG0xmXge8lEi5513WEpF3UwgRmQBOOnkSeCne1LyUoCtyG8GSjSXY3jsMZ3dHFjbWzv/Q9bFL398UqZ02N6ST4QsaXje9pnJ3xhzP+G2vH/CSL7R6ffnw8RawNJFyO8KuTaRUKYSITCAnnXSB7cD2eFNzI0F35LPAXIJ7R7o40x1Jnci2p04AK6PT5zTUzb/xmtjs+U1V02cvmMIlm4LmxkyvsOF1Od/mUqf93S+0esnksZwhCB9JgvDRHnJ5IiVPIURkkjjp5AmCg89e4be7IxDsSMmQDyS5vpP9/buWbQe2E4lGaq/80Lyay69tqpr5vqZo3bQ5k1hmQRN06yvkoLLMsO3ZdDy3+Znd7s72fjsdqAbWo/AhMqEUQkQm2RjdkY8AzQSTeyFYqukifxgYfs7PHxF/GFhedcnc6bVX3nhNbPaVTVXTZl9tolXVE1jeeE9LzQHUV5fvcoznW+9Qt59a93ZuRyLlHfUtswkG960GVip8iEw8hRCRKZTvjrwKvBpvap5BcPjZR/KPkXAx0iUBwOvp6Ovv6dgKbMVETPXsqy6LzZrXWDWjcW60/tLGSN30xkh17cWe3zGeTshM8gEpXmadEN9aezxjD206ltv14l63tXuIBqABqAWeAt5KpNzM+d9FRC6WQohISJx0shfYAmyJNzVXEXRGFhF0SeYTLNUMEXRJPACsb7MnD57Knjx4imBnDgCR+Iza6jlXN8Zmvq8xOm1WY7T+krmR2obZJhK90OmmBR3ZXi7D6045fsf2Dn9nIuXubuuxLjCL4L6dVuA1YE8i5XqhFilSARRCRIqAk056wMH8Y0m8qXkmQZfkZuDDBDdEGoJg0p9/uCOv953eoVFLOAFjTGzW/Etjl82bE43PmB6pqW8w1XUNJhqbVTV9Vr+JxmYS7Ny5kDMhpLaqNDshnm+9Y322bU9nbt/qtlx67yl/gCB4zCT4s3wV2JBIucdDLVSkwiiEiBQhJ53sBjYBm/Jdksb84wqCOTYf4J3zOyIEHZOB/CM4qdNa63a2nXY7286+7+MK4HtOOnlknOW8M7yuhDoh/Vnbe6DLT29pz+1bftA71J/FBy4j+HrqgDcJttnuT6TcXJi1ilQqhRCRIpfvkhzLP7YCxJuaDcFNkyPhZEH+cQVBCDEE4cQFsvnHcP5jAzgFlNAAnJpWTawqYor2e0bvkO06lvHf3t/lH9lyPPf2tg7/FMF9NpcC7yP4c9kBrAVaNVROJHxF+w1FRM4tf1prb/6xj+DUTuJNzTFgNkEwmUmw5HAZwQ/iS/Of6yXomFzQHQtjVQQ3aebmNkQaJvaruHieb93OAdv+dq9/ZO8p/8ibR3JH2vvtSLCaTtDtmEfQIUoC2wg6Hv0hlSwiY1AIESkj+e3Ax/OPd8l3UKL57sp4nDmyfXb91N8Pks3ZbM+Q7Tzl2M72jO083Ot37j3ld6ZO+T356XAGqOedwAVwFFhGcJPpES21iBQvhRCRCpLvoBSy6yNOMJyNadWmJufbXDRiohNRi+dbz3HJDGRtpj9rM73D9PUM2cxpx2ZODviZth7bk+7ye896WRVBp+NK3ll2OgpsBNLAIc1wESkdxlpNmxaRsd2xMHY1cDfBD3oAplUTm1Nv6mbWmdqaqIm5S4N1AAABv0lEQVRGI0RiEaJVEROJRohU5R8GzHAOz3Ft1nFx+7M225+1bmaYbN+wdV0/CDfnECUIQPVADUEQMgT3tqSAXcBh4Ggi5Q5O0pcvIpNMnRAROZ8zR7aPyGRxM1nr0m37LvI9R2aw1BDcOFqT/9jnne6GRxB8tgNtQGf+0Z1IuecLLyJSQhRCROR8svlf5zGy9ffdzKhfRz9nrOdH8r9mCA5h6yQ4MO1k/lpf/uOeRMpVm1akzGk5RkTO646FsVqCczVGfo0RhIkIwbJJ5KyPcwThxeWdLcKjtwo7ullUREAhREREREISufBTRERERCaeQoiIiIiEQiFEREREQqEQIiIiIqFQCBEREZFQKISIiIhIKBRCREREJBQKISIiIhIKhRAREREJhUKIiIiIhEIhREREREKhECIiIiKhUAgRERGRUCiEiIiISCgUQkRERCQUCiEiIiISCoUQERERCYVCiIiIiIRCIURERERCoRAiIiIioVAIERERkVAohIiIiEgoFEJEREQkFAohIiIiEgqFEBEREQmFQoiIiIiEQiFEREREQqEQIiIiIqFQCBEREZFQKISIiIhIKBRCREREJBT/H9WXF1lcZJfoAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels= data['Segment'].unique()\n",
    "plt.figure(figsize=(8,6))\n",
    "plt.pie(grp['Quantity'],autopct='%1.1f%%',labels=labels,explode=(0.05,0.05,0),shadow=True,startangle=80)\n",
    "plt.title('QUANTILIES ORDERED BY EACH SEGMENT',size=25,color = 'GREEN')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Cities of least and most quantity ordered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "        34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]),\n",
       " <a list of 49 Text xticklabel objects>)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 648x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    " sns.catplot('State',kind='count',data=data,palette='rocket',height=6,aspect=1.5)\n",
    "plt.xticks(rotation=90)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Grouping by Quantity of Cities"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Quantity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>386</th>\n",
       "      <td>Port Orange</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>259</th>\n",
       "      <td>Littleton</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>257</th>\n",
       "      <td>Lindenhurst</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>140</th>\n",
       "      <td>Elyria</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>213</th>\n",
       "      <td>Iowa City</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>221</th>\n",
       "      <td>Jupiter</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>222</th>\n",
       "      <td>Keller</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>171</th>\n",
       "      <td>Grand Island</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Baytown</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>203</th>\n",
       "      <td>Holyoke</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>388</th>\n",
       "      <td>Portage</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>218</th>\n",
       "      <td>Jefferson City</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>275</th>\n",
       "      <td>Manhattan</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Atlantic City</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>110</th>\n",
       "      <td>Danbury</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>227</th>\n",
       "      <td>Kissimmee</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Billings</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>417</th>\n",
       "      <td>Romeoville</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Abilene</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>441</th>\n",
       "      <td>San Luis Obispo</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>309</th>\n",
       "      <td>Montebello</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>288</th>\n",
       "      <td>Melbourne</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>304</th>\n",
       "      <td>Missoula</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>Conway</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>463</th>\n",
       "      <td>Springdale</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>73</th>\n",
       "      <td>Chapel Hill</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>398</th>\n",
       "      <td>Redding</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>70</th>\n",
       "      <td>Cedar Rapids</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>Commerce City</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>90</th>\n",
       "      <td>Coachella</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Baltimore</td>\n",
       "      <td>184</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>Fairfield</td>\n",
       "      <td>185</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>194</th>\n",
       "      <td>Henderson</td>\n",
       "      <td>198</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>299</th>\n",
       "      <td>Milwaukee</td>\n",
       "      <td>201</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>Lakewood</td>\n",
       "      <td>204</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>295</th>\n",
       "      <td>Miami</td>\n",
       "      <td>215</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>267</th>\n",
       "      <td>Louisville</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>375</th>\n",
       "      <td>Phoenix</td>\n",
       "      <td>224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>74</th>\n",
       "      <td>Charlotte</td>\n",
       "      <td>243</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>434</th>\n",
       "      <td>San Antonio</td>\n",
       "      <td>247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>262</th>\n",
       "      <td>Long Beach</td>\n",
       "      <td>256</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Aurora</td>\n",
       "      <td>258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Arlington</td>\n",
       "      <td>259</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>93</th>\n",
       "      <td>Columbia</td>\n",
       "      <td>316</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>215</th>\n",
       "      <td>Jackson</td>\n",
       "      <td>318</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>407</th>\n",
       "      <td>Richmond</td>\n",
       "      <td>336</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>330</th>\n",
       "      <td>Newark</td>\n",
       "      <td>362</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>216</th>\n",
       "      <td>Jacksonville</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>Detroit</td>\n",
       "      <td>441</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>109</th>\n",
       "      <td>Dallas</td>\n",
       "      <td>555</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>464</th>\n",
       "      <td>Springfield</td>\n",
       "      <td>649</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>437</th>\n",
       "      <td>San Diego</td>\n",
       "      <td>670</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>Columbus</td>\n",
       "      <td>836</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>Chicago</td>\n",
       "      <td>1132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>207</th>\n",
       "      <td>Houston</td>\n",
       "      <td>1466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>452</th>\n",
       "      <td>Seattle</td>\n",
       "      <td>1590</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>438</th>\n",
       "      <td>San Francisco</td>\n",
       "      <td>1935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>374</th>\n",
       "      <td>Philadelphia</td>\n",
       "      <td>1981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>266</th>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>2879</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>New York City</td>\n",
       "      <td>3417</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>531 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                City  Quantity\n",
       "386      Port Orange         1\n",
       "259        Littleton         1\n",
       "257      Lindenhurst         1\n",
       "140           Elyria         1\n",
       "213        Iowa City         1\n",
       "221          Jupiter         1\n",
       "222           Keller         2\n",
       "171     Grand Island         2\n",
       "32           Baytown         2\n",
       "203          Holyoke         2\n",
       "388          Portage         2\n",
       "218   Jefferson City         2\n",
       "275        Manhattan         2\n",
       "22     Atlantic City         2\n",
       "110          Danbury         2\n",
       "227        Kissimmee         2\n",
       "40          Billings         2\n",
       "417       Romeoville         2\n",
       "1            Abilene         2\n",
       "441  San Luis Obispo         2\n",
       "309       Montebello         2\n",
       "288        Melbourne         2\n",
       "304         Missoula         2\n",
       "98            Conway         2\n",
       "463       Springdale         2\n",
       "73       Chapel Hill         3\n",
       "398          Redding         3\n",
       "70      Cedar Rapids         3\n",
       "95     Commerce City         3\n",
       "90         Coachella         3\n",
       "..               ...       ...\n",
       "28         Baltimore       184\n",
       "147        Fairfield       185\n",
       "194        Henderson       198\n",
       "299        Milwaukee       201\n",
       "240         Lakewood       204\n",
       "295            Miami       215\n",
       "267       Louisville       221\n",
       "375          Phoenix       224\n",
       "74         Charlotte       243\n",
       "434      San Antonio       247\n",
       "262       Long Beach       256\n",
       "24            Aurora       258\n",
       "16         Arlington       259\n",
       "93          Columbia       316\n",
       "215          Jackson       318\n",
       "407         Richmond       336\n",
       "330           Newark       362\n",
       "216     Jacksonville       429\n",
       "123          Detroit       441\n",
       "109           Dallas       555\n",
       "464      Springfield       649\n",
       "437        San Diego       670\n",
       "94          Columbus       836\n",
       "80           Chicago      1132\n",
       "207          Houston      1466\n",
       "452          Seattle      1590\n",
       "438    San Francisco      1935\n",
       "374     Philadelphia      1981\n",
       "266      Los Angeles      2879\n",
       "329    New York City      3417\n",
       "\n",
       "[531 rows x 2 columns]"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftop10 = data.groupby('City')['Quantity'].sum().reset_index().sort_values(by='Quantity',ascending=True)\n",
    "dftop10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Top 10 Cities with Highest quntity"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Quantity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>464</th>\n",
       "      <td>Springfield</td>\n",
       "      <td>649</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>437</th>\n",
       "      <td>San Diego</td>\n",
       "      <td>670</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>94</th>\n",
       "      <td>Columbus</td>\n",
       "      <td>836</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>Chicago</td>\n",
       "      <td>1132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>207</th>\n",
       "      <td>Houston</td>\n",
       "      <td>1466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>452</th>\n",
       "      <td>Seattle</td>\n",
       "      <td>1590</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>438</th>\n",
       "      <td>San Francisco</td>\n",
       "      <td>1935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>374</th>\n",
       "      <td>Philadelphia</td>\n",
       "      <td>1981</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>266</th>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>2879</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>New York City</td>\n",
       "      <td>3417</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              City  Quantity\n",
       "464    Springfield       649\n",
       "437      San Diego       670\n",
       "94        Columbus       836\n",
       "80         Chicago      1132\n",
       "207        Houston      1466\n",
       "452        Seattle      1590\n",
       "438  San Francisco      1935\n",
       "374   Philadelphia      1981\n",
       "266    Los Angeles      2879\n",
       "329  New York City      3417"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftop10.tail(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 1440x720 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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g7Ky4C7K+9bZWrdzxXgxSpJ+ZXuz2jliZZJupvTdmQ9cNRGnnaXAExERERExgCRd3uO0be897mFiRJI2H+55278cryzx7ElabPtFtXNEf5LW6Qy9mWhS4ImIiIiIiFjFJE0FPgBMA24BzmgGqsQAyQqe9pK0J3AGZYrxZpJ2Ad5v+68qRxs3KfBERERERAwoSX8G7ABM7ZzLuO12kvRt4EngamA/4Je2j6qbKnqR9AhlO91KTwFr2U4v2xaS9GPgIOAC2y9tzk2opub5ixkRERERMYAknQqsDcwCTqdc2FxfNVQMZ3vbOwFIOoO8V61le73aGeLZsb1YUvepp/r97upoUu0AERERERHxrMywfRjwkO3jKaOc0xukvZ7sPMjWrIhVYrGkGYAlTZH018BPa4caT1nBExERERExmB5rfj4qaVPgAWDLinlieLtI+l3zWMBazXFnitb69aJFrBY+AJwMvAD4NTAX+GDVROMsBZ6IiIiIiMF0kaQNgBOBhZSeIafVjRT92J5cO0PE6sz2EuDttXPUlCbLEREREREDTtKawFTbD9fOEhExniR9cpinbftT4xamsvTgiYiIiIgYIJJ2l/T8ruPDgHOBT0l6br1kERFVLO3xB+Bw4G9qhaohK3giIiIiIgaIpIXAPrYflDQTOAc4ApgObGf7oKoBIyIqkbQecBSluHMu8AXb99VNNX7SgyciIiIiYrBMtv1g83g28DXb3wW+K2lRxVwREVU0qxePofTgORPY1fZDdVONv2zRioiIiIgYLJMldW7UvhaY1/VcbuBGxIQi6UTgJ8AjwE6250zE4g5ki1ZERERExECRdCzwemAJsBnlTrUlTQPOtL1X1YAREeNI0tPA48AyyjTBZ56iNFlev0qwClLgiYiIiIgYMJL2ADYB5tpe2pzbBljX9sKq4SIioooUeCIiIiIiIiIiBlx68EREREREREREDLgUeCIiIiIiIiIiBlwKPBERERHDkPR8SedIulPS7ZIuljRT0nnN89Mlvb52zoiIiJjYUuCJiIiI6EOSgPOBK2xvbXt74BOUqRwHNb82nTLRKCIiIqKaFHgiIiIi+psFPGn71M4J24uAxZJulTQFOAGYLWmRpNmSfi5pIwBJkyT9l6QN68SPiIiIiSIFnoiIiIj+dgRu6Pek7SeATwLftj3d9reBbwBvb35lH+Am20tWedKIiIiY0FLgiYiIiPjD+hfgsObxu4GvV8wSERERE0QKPBERERH93Qa8bCwvsL0YuFfS3sArgEtWRbCIiIiIbinwRERERPQ3D1hT0ns7JyTtDmze9TuPAOsNed3plK1a59p+apWnjIiIiAkvBZ6IiIiIPmwbOADYtxmTfhswB7in69cuB7bvNFluzl0ArEu2Z0VERMQ4UfneEhERERF/KJJ2A75k+1W1s0RERMTEsEbtABERERGrE0kfA/6S5ZO0IiIiIla5rOCJiIiIiIiIiBhw6cETERERERERETHgUuCJiIiIiIiIiBhwKfBERERERERERAy4FHgiIiIiIiIiIgZcCjwREREREREREQMuBZ6IiIiIiIiIiAH3f61p0C90oJfzAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (20,10))\n",
    "sns.catplot('City','Quantity',data = dftop10.tail(10),kind = 'bar',height=8,aspect=2,palette='cividis')\n",
    "plt.xticks(rotation=90)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Quantities Ordered Region Wise"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Region</th>\n",
       "      <th>Quantity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Central</td>\n",
       "      <td>8780</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>East</td>\n",
       "      <td>10618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>South</td>\n",
       "      <td>6209</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>West</td>\n",
       "      <td>12266</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Region  Quantity\n",
       "0  Central      8780\n",
       "1     East     10618\n",
       "2    South      6209\n",
       "3     West     12266"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "region  = data.groupby('Region')['Quantity'].sum().reset_index()\n",
    "region"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = data['Region'].unique()\n",
    "plt.figure(figsize=(8,6))\n",
    "plt.pie(region['Quantity'],autopct='%1.1f%%',labels=labels,explode=(0.05,0.05,0.05,0.05),shadow=True,startangle=80)\n",
    "plt.title('QUANTITIES ORDERED BY EACH REGION',size=25,color = 'green')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Highest Selling Categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Quantity</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Furniture</td>\n",
       "      <td>8028</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>22906</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Technology</td>\n",
       "      <td>6939</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Category  Quantity\n",
       "0        Furniture      8028\n",
       "1  Office Supplies     22906\n",
       "2       Technology      6939"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat = data.groupby('Category')['Quantity'].sum().reset_index()\n",
    "cat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Distribution of Products Sold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = data['Category'].unique()\n",
    "plt.figure(figsize=(8,6))\n",
    "plt.pie(cat['Quantity'],autopct='%1.1f%%',labels=labels,explode=(0.05,0.05,0.05),shadow=True,startangle=80)\n",
    "plt.title('DISTRIBUTION OF PRODUCTS SOLD',size=25,color = 'green')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Most Profitable Categories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Category</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Furniture</td>\n",
       "      <td>18451.2728</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>122490.8008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Technology</td>\n",
       "      <td>145454.9481</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Category       Profit\n",
       "0        Furniture   18451.2728\n",
       "1  Office Supplies  122490.8008\n",
       "2       Technology  145454.9481"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat = data.groupby('Category')['Profit'].sum().reset_index()\n",
    "cat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAcoAAAFtCAYAAACHhSqKAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nOydeZgcVdW431O9zF6zZScJIdtAoAkTAiEJkBDC5sgIgsgOKkoQBEFRVLSnXQcEUT8RFD9hfirKJ4oiqIgiLiCKihJc2GQCyBogezKZnr6/P251pqdT3bN2V8/MeZ+nn+quqlt1qrrqnnvOPfdcMcagKIqiKIo/TtACKIqiKEopo4pSURRFUfKgilJRFEVR8qCKUlEURVHyoIpSURRFUfKgilJRFEVR8hAu9gklISuBXwOYuJFin38gSELSY2aOMHFzf8b6WcAz3s+9TNx0FlWwASIJaQPiwG9M3KwMVpriIgmJAR8HDgMmAiHg7yZuDghUsBFGEvIO4D3AvkCNt/pSEzdflITcApwDdJi4OTcYCRVlYIyGenVAijKj4s3EAFuATcCzwCNYBXiniZudIyhjf7LNAs4FMHHTVqzzBoEk5ADgBGCDiZsvBi1PqSEJ2Qt4gF7F8TrQDawfYPlZ9L6wmaSAjcDjwM+Ar5q4GdAxC4Ek5APANd7PJPAK9n3cOoCy5wKzgPszG4HFRhJSBpwBHAcciG3URLH/2T+xdcl3TNz4/R9DPecsxkldoYwsQ7EoX874XgFMA/YAlgLvBV6ThHwcuNHEfbMZbMNWOCPFLHqVeNsIHTMt37YROt5IcQD2WtcB+RTleuw1PFsMoUqI87FK8imsN+D5YRxrE7Dd+x4F6oFDvM+FkpAWEzd/Ho6ww+CD3vLLwAdN3HRnbX8R+/+/6FP2XGCF9/3+QgjXH5KQNwM3YuuNNF3Y920yMAVYBbRJQr5u4ua9I3TqWYx8XaEMn25669zsZ7kkGLSiNHEzJfO3JCQELACOAi4C9gK+ChwqCTkzW1mauPkTsPeQJS4CJm5KWr7+MHHzFeArQcsRADFv+eNhKkmAS0zc3JL+IQmpxzYE48Ak4IeSkPkmbnYM8zyDQhIyEatIAG7yUZKYuPkI8JFiyjVQJCHnY+sHB3gOaAd+YuLmOW97BNsYeTtwHnA69r4rYxQTN/+lxHXCsPsoTdz0AGuBtZKQG4H/BU7FPuCPAZ8b7jkUZYBUesstI31gEzdvAJ+RhJQDVwIzgLcAt430ufqhMuP7iF9nIZGELMc24Bzgt0CriZuNmft4iv93wO8kIVdjlaqiBIoMJNdrZh9lfwE4kpAo8BDQjHVf7WXi5vWM7SvJE8wjCdkbuAxYCUwHBOtK/C9wH/D/TNz829u3E9gzjzi7ghmyA1wkISdhXXUHABOAT6b7LQYazANEgI8Bq7F9LC8DPwU+5bWSsq/tXOBmYJ2Jm1l+Aufq2M6QKReJDPn7XGuO8zQDl2LdcJOxbsZ/Af8H3GDipqs/+SUhBwIfxgbONGD/ox9hr/+NfuTNiSRkDta9uBr7DHRj3ak/Ar5o4mZT1v6d5H8O+vyPec47i957/45MizJjn/n0uomuNXHzQW/9SjKea+/+fpDe+/tA9n8hCXkr8E7gIKxr9w3gYeB/TdzckbXvruPnYNcz5RfMk/Hf5SPzeasALgROwrb2q4ENwKuejHeauPlBP8frgyTkIWAJtk9134H080pCHBM3qYzfEWzdcDywDOu+bfRkewS4BfhetidrMHVFRplybMDUSdigKRfbh/oQtmvp53nkrgI+BJyCdfluBv6MfWZ+lSFPruesHFjjld8H2831MvAb4Asmbv6W47y7jgvc7slwoidDNbbe+h72f7ghn1tbEnIk8Ets//dcEzf/kYQ85t2L93meq8z9lwIPej9/YOLm5KztEewzXgUcaeLmPm/9LPIE80hCpgMfAI72riMMvIbtWvgtcKuJm4dzXMNKbD2/HOsJ6sK+v7cD15u46bdfHwowPMQL5Pms99PFBp8MCEnIUcDfgHcD87A3ZAe2slyCdSedmlHkVeyNT/Ny1qdPazXjPNdib9Rq7xwpv/36YQnwF2yFVAv0YK2M84FHJSGLhnDMfLyMbXiAlTf7WgdsXUhC3o+V/SxgJvYeV2H7ma8D/iQJmdrPMU4H/gC8DfsSh7Ev4aVYa6B6oPJkHfcU4B/YSmIuVklGsQ2vBPCYJGSfrGKvYu9B2g25lb73ZiSDyzJduq7fDl4j7I9Yr0oNNuAmc3tUEvI94AdAC7ahtsVbtmDdurd6FUuandhryVQu6+m9xlf7kXs7+e/Ry9hnGElIDfa//TzWDVrryVeHrbTPBq7t53x9kIQchH1nAP5noMFQmUrSYznwC+B92CCgemzlNxFbkd4K3CYJya7bBlVXSELmAY8CXwIOxzYE032obwF+JgnxtXYlIZOAPwGfwDYyQthG9XHAvZKQNfmuWRKyB7Yxch32nazCvqMzse/sXyQh78t3DGzj4S/YCPD59H0Gb/SWZ0hCKrMLZvBub/lLEzf/8b7f5y1X+eyfuW6lJCTbEDoYey1d2OerXyQhC7H/w/uxXXxl2Gd3CrDIW3+hT7mwJOQmbOPyVGzd3O2d/yDgKux9zNd42kWhxlH+HO+lozdwYCB8FXsjfgHETNxETdzUYyviGLYDfl16ZxM3BwFvzfg9Jetzic85DsRarFcDk03cNGBvXn+t7Wy+hm0FLTFxU+Md4xhsAE0DcIdX4YwIXt9w+nqe87nWa/KVT+MFUlyHtdR/DMw2cVOHbW2ejW357g/c7vU/+zER+CbQAcz0ytdg+6i7sS3ODw32Gr3Gxbexz8ADwEITNy7W3diKbUHOAH6SqYhN3Bzk3Z90a/aarHvzICPHrIzvr+fY5xbgXmAfEze1Jm4q6K10wDYk345tqX8KaPSewwn0NjJP87YBYOLmQe8aD8o4zkEZ15i5fjdM3NzWzz2aku4nxD5nC73rOwmo8N7DMqwFdzb2HR0MR2Z8vyPnXv2zHasMW7CVZYX3/jV6cm/CNt4uyiw0mLpCElKHvb55WMVwuHeeOmxj4TJsw+ECSYhfHdOBrdS3A+8Carz7NxPrsfkS9h3aDe+d+wGwH1Z5nwlUe+eeA9yFrbe/LAk5Ls99asM25N7qla/HvjuvYLsL3vC2vz2HHBOwlijYui5N2qux0qcxcoS33IT9Pxbm2P6QiZvtDIxrsY2hv2IbDRHvXSnHNgA+iG1YZ3MNto/7ZWwfd6P3nFR4cjwCNGEbpf3qwYKMozRxs0US8h/sgzZnIGW8Vthc7+e5Jm52Rex5AROPeZ/hUo11XXw44/hdZCjgAZIEjjJx84p3DAP8QhJyLNYqnom1ij4/AjKPJFd5y98DJ3l9zGlPwLckIRuAO7FurROxlnc2lVhX1a7K38TNNuB6SchsbEVyGrZFPRg+g215PwUc7R0zbVX8RBLyPLalPgd7bwfUOBhhMl1VD+XY55/Y/rd0YxETN0/CLmshXbm2m7j5RMY+bwAf89xulwGXSUK+lPkuFIll3vIaEzc/zJAvBbwAfMv7DIZ9vWUX1sU/JEzc/BE7rCR7/etY5fEC8H3gYmxU8FD4GLZBdB9wjImbXdaY16d6nefi/CFwpSTk+vQ+kpBDgWO93d9j4ubbGWWf8zwxv6RXaWRzMr2W99tN3NyTUf4/kpATse/uEmxj/2c5jlMBHG7i5pGM8ru8IZKQDqw19h78jYRzsJ6cl7H1QZr7sR6temy31V+945Vhn5ttwNexCmwVti5Mk7Y483UhZJN+Fi8ycbPrffPqqyfx8WxIQvbD/v/bsHX02oxy3cD9kpAV2Pd0EbYR/qN8QhQyM0+6td0wwP030+sCzev2GyYpepXFcLgxrSQzMXHzL3qVy6nZ24NEErI/tqULth+xJ3sfEzc/wSojsMouF5/Osf7H3nJuP26dbNnqsBY5wOfTSjJLtkewlVN/so0onqt0H0nIl4ELvNVPYlv3fnze7956nERvl0J7jn0+jVUoEWzFWWw2eMuRfA8b08f2caeOJHd7yzn9dR/44bkL3+n9vDZTSWbxI6zlNAHrpUrzNm/ZCXwnu5B37bneHei18P6QqSQzyiexXRAA+4lNsOHHzzOVpA9p9+shOY5xnrf8psmIrPYac3/3fma6Wg/BKucHsB7FPts9RbrU+zkYRTmUZ/FdWI/Z3ZlKMhMTN5vpVY7H+O2TSSEz8wwq646Jm+2SkF9hh5n83IugvRt4xIxsAoOn/BTcELivn22nA/tLQiLGJ4Q/IBZ7yyQ2KCAX92L7Exbn2P66iZuncmx7IeN7PQMfi7qI3mfml/3IdgqFv7c3S0JyueOfwVqMuSrRB/IcN31PHzZZQUlpTNy8IQn5M7Y/Ltd/UEjuwjZELvKGo9wG/H6g/Yo5SP+3w54p3uvSWAO8GdtnWodtVGSzB/5jSfOxgN7G/S2SkHxKPe3+3xPbJw32OQb4rfEfRw72+UjiX/+m/+9878CvsV1bIW9/P2WQ7xnExM3jkpBfYy3bd2MtMAAkIYdh+1YN8A2f4vdhYwZW0evVWZWx7UFsQ+9wSUjYe0+WYd2l2+m9VwPhLk++DrFR03di35189cqh3vI4SchLefbL/P/yUkiLst5bvjaIMudhWysTsZ3QDwGbJSG/l4RcLgkZqHWaj5FQkmAjPPvbFmbgFnUxmOQt1xufqNYM0i6aSTm2b85TNlN5+FVeucg8V757m5at0Pd2E72BHi8A/8a+pO/F9p//O0/ZfM9Y+jrzXSP0/x8UDBM3t2L70QzWK3IH8Kok5ElJyPVetPNgSSvZ+oH0CeXCizr+J9bteDi2ruimN6ArMyFK1RBOMS3j+0Rs8E6uT/o6KrPKQN8GYx+8dy9Xo6Pf58PrikqXz/V8DKSeS1uVZ3lRzmne4y3vzQjiySRtER4mCUkr+7Qr+T6v//EhbNzC4qztD/ZT92TzIe981djuiPuBTZKQP0tCEl5XRjbp/7Ca/P9f+vno1/NVEIvSC7SY7f18eqDlTNw86wV0HAW8CduiXugtlwMfkYScbLyw4iGSyyU2WIbdMg6Qgcpe6tdYSPn6JBwYDHncrn12G+jhhiLDcDFx835JyFewrsTDsG6zud7nvV7f6fsHcch0wEUZ1gr0C8AYCDdjo+A7gcuxFXPm8LMQvY21oeSSzgxgm2Li5uWce/ozUMu5P9mG+3wM5Bm8A3gJGxT1NuD/eV0gaXf/13OU+y32HlcDB0tC/obtM92IjbQFa1muwFqaD9HX4hwwJm42AKu8vt/j6fWyHOh9LpeEvMvEzXcziqX/wytM3IxEN1vBLMpj6RX2/sEUNHGTMnFzj4mbS0zcLMZaDWdgo0nrgVvFjtUMmul5tqVbOUn6RkamX+DyPGVrhyNUP6RbmRO9PoNcpK+tvyEHI0lmCzjfvU1vS9I33H+0kL7OGf3sF8R/0AcTN0+ZuPmciZs3YfsYl9Lbr3OJJKR1EIf7Vcb3E3PulQdJyAx6gztOM3Fze6aS9JjC8Mh01eXq/8tH+v+dlmsH791rzLG53+fDC/ZKlx/y8+F1W3zT+5kOzDsLWz+9RN8gnsxym+lViKuwrs4o1t2cVtBpq3OVN6b04Kz1g5X19yZuPmzi5lCsq/0tWJdzBfBNScjkjN3T/+FQ/j9fRlxRekrso97PjfQTTdQfJm42e66gd3mrJtP3BmQORi7mbCS5otYytz2a1YeWrtgn5VFUS3Ksh95rHep1pnOThsk/bGe1t/QdxFsg/krv9R2ZZ7+0bH8vob7fwZD+DxZLQnwbRV6rfldf5giff0jPkNeAfQhrbaRzCB81iPIP0xskdpE3/KBfsty0mcojV6DK6hzrYWB1xWP0jlceSjDeX71lvvdrObm9eennI987sDKj/HCfj69j78uh3vjktMK8uZ/3a5ciJMPtmrH9IWx8wjLstUSwQ2qG/TybuNlh4uZOeof7lNPbLwm9/bMtQx3Pnc2IKkrPz30LtqMX4HOe6TyQsv1ZiZnjbjLdCpkBEXUDOdcIscbvZZeENNHrushOb5aOFhN8WtXe/bs0zznT1zqk6zRx8yi2fwdsWPtu4yQlIW+iV1l/N3t7ofCek3SU3+V+EbPe4OOTii3bCPMDrDVcjs1q5MdHsS7Kbm//kaTfZyift8GzGNLBdYPtxvigV2Yy8INcDYUMOabTt6GdmRQge4xeOsjnyjyH7Leu8AJP0lbWOZ7LL5+M2f3k6Yj3Wd5QkOz9hV5Dwo/veculkpCjfcqH6R129ZiJm2ENmTNxs47eISY3Yo0QA9zUT9G0UlyKTaSQuS5trT6AtfjS1/v7PAFwu+ElDcino3LphJuw11BHP8PzJCGRgSjTYStKSYgjCdlPEnIZtt8hHbb/LWyH+0BZJgl5VBJyqReK73jHF0nIMuAGb7/n6Rvl9QS9L+55RbQqI9gsGwdlyLkaW9mXYRM+35hZwBvH9Hvv5xckIavTysoLkPgl+YM30i+FKzaDzVBIV86HYZMK7OWdPyIJOYNeBfQgw/QGDIGPYZXDXOCedNi694y9CZseMIzt9/5azqOUMMamNvyS9/MKLyChDqwlKQn5FLbvDex435EeQ5l+ht6UIxAC4I+SkC9LQlZ6bjM8+aZJQv6H3vHOPx3MiU3c/A47htRgA3EelYRc4CnE9DkikpBlkpAvYt/twzMO8U96rdlvZgYViU2fdj+9QYR+DLSu+BT2GQtjI/Av86J/0+eqlYQcK3Ys4u98rvFe7+dNkpBz0w0P7zq/g333ckVt/oDeqND/k4ScLl6GJu9d/QG9wywGndQjB+l6Kn2v7zX9T2/2APZelmMbLevZPfo2rTjTDe/Bul2nA09KQq6UhDRnBA6lh7qlx6huxfabAmBser/07EprJCHfl4QckP6/JSEhSchCsbNcPY0dD5qXQStKSchLGZ83sBXbWuzAz72wN2yNiZuz84RH5yIGfAH7QuyQhKzH/hkPeNs2AadnDeTeRu/g56uBLZKQdZKQTklIIQekn48d+P4nSchmrFvhXmyo8QbgrTnC/9+HjRqd6u2/RRKyBetymYPtI/DFG5KR7uu5TRKyybvOTrFp6frFxM1d2Ogxg00v+B/vf9yCffBc7P/5tgEGpYwY3rivs7D/+aHYinQj9kW4G9vv8xxwvImbUZUQPIuPYjO0CNY6eE0S8jo2QjxtEX0XG/k90nRgx3DOBZ713uP0M5RWWHXY5/TX2KjzN7xn9L/0Zry5zsTNYLPzYOLmeqw35UVsUo6vAs9JQrZ796AL+75fgm2M3pxR1mDTlSWxCQz+LAnZKgnZim3Y7U2OTDNe+QHVFV6/51FYD1AVtm57xbsPG7Hv98+wGYr8PGFnY6OkKz35N3vv2HOefBfRG7XaZ/YZ7507CWt01GIV6xav/H+wg+NT2GCzXMkGBstP6ZtwJVcQT6ac2+g7zOPXPvV9tmIcSv/kbGzD5a9YnfCaJKQL+9+sxNYV5/r0VV9Or7I8Geuq3+bplB3YRAifxLrz+9VTQ7Eo06G1k7Atrpew/ugbPIH2MHEzlNb+w9jxcTdgO4rXYx+U9EVdjU0J9jufshdiUzalW8szsQprQP0gQ+SP2H6k/4d1CYWxFclN2OEDvnMVeq2dg7Eullew/8F64Hpsy+affuUyOBmbgu4JbEWyp/cZsDvWxM11nuzfxr68lVg3xkNYJXqwiZuc4e2FxMTNbdhK8GvY1l4ZtmL8GzbR+35eUodRi4mbnSZu3o6tEH+GVZA13vJn2EbW6YXogzU2Q9AR2ECNV7FBIelnKN1iPxV7r3+FHTMaxT5r67DdCUeauLlsGDL8GFsBvhubQKIT6zqrwr4Tv8J6F2abuLk0q+xdWMvnbqzCCmPfn5uBRSZuMoOG/BhQXeFZVIuxSu8urGKvwt6LZ7ARo++k17rLLPsSNtXgp7HvaQr7DP8UWGXi5iZ6g/Z265ryvA6Lse/iQ9h3sxL7rn4LONDEzVCzDu2GlwQhncgjZxCPD5mKzy+a9c/0urs30dt/O1D+i20YXIe9Dy9iI22T2Hryemx9sFv2MBM3Pd6zswir+B/HPmO12FiRB7DPwQEmbvKOOYUBzh6iKIqijAxiE64/4f2caXpz7AaGJORRrNfucyZu8vWhjksKmXBAURRF2Z30pNr/LBEluRKrJFMMwO06HilkCjtFUZRxh9g5dT+I7ZZ5xBt3mF7/YeBcb9dcuX6LhtjJKNJ9ebebrLkgFYsqSkVRlJGlHDvu+10AXgBQhL6p0r5s4mawM7CMGGLnQ12OTdAQxgYYXhGUPKWOul4VRVFGlqexFuXPsYE/YWymsuew0c6rjf9cucVkCnb4xVbssLSVAxgSMm7RYB5FURRFyYNalIqiKIqSB1WUiqIoipIHVZSKoiiKkgdVlIqiKIqSB1WUiqIoipIHVZSKoiiKkgdVlIqiKIqSB1WUiqIoipIHVZSKoiiKkgdVlIqiKIqSB1WUiqIoipIHVZSKoiiKkgdVlIqiKIqSB1WUiqIoipIHVZSKoiiKkgdVlIqiKIqSB1WUiqKMOCLSIyJ/y/jMGqHjtorIFd73E0RkwUgcV1HyIcaYoGVQFGWMISJbjDHVQywbMsb0DGC/W4C7jDG3D+LYYWNMcihyKeMXtSgVRSkKInKuiHwl4/ddIrLS+75FRD4pIn8ElopIp4gkROSvIrJWRPbOPIaILANagc97FuscEblfRBZ7+00Qkc6MMt8XkZ8Av/DWXS4iD4vIoyKSKOZ9UEYfqigVRSkEFRlu1zsGsH8V8JgxZokx5vfeuvXGmEXADcAHM3c2xjwI3Alcbow5wBjzdD/HXwqcY4xZJSJHA/OAg4EDgANF5PBBXJsyzggHLYCiKGOS7caYAwaxfw/wg6x1P/SWfwHeOkx57jXGvO59P9r7POL9rsYqzt8O8xzKGEUVpaIoxSJJXy9Wecb3HT79kl3esoeB1VWZxy/P2rY147sAnzPGfG0Ax1QUdb0qilI0OoEDRMQRkRlY1+dw2AzUZB3/QO/7yXnK3QO8U0SqAURkDxGZNExZlDGMKkpFUYrFA8AzwFrgGuCvwzze94DLReQREZnjHfMCEXkQmJCrkDHmF8CtwB9EZC1wO30VrqL0QYeHKIqiKEoe1KJUFEVRlDyoolQURVGUPGjUq6KMQWZdcfcxwLeBp30+/+5sb1kfoHiKMqpQRakoY5M9sQEtE4Al2RtnXXH308AfgAe95drO9pZ+08YpynhEg3kUZYxQOW/JNOB84I26FeceGp0w86RBFN8CPEyv8nyos73ltQKIqSijDrUoFWU4tNVOAmYDc4BpgIsdalDtLbO/p3+HgR3A9ozl9hy/NwD/zfo8R9vG7VnSzPTkeJ1Uz8JBXkk1cIT3AWDWFXc/gVWcfwDu62xveXKQx1SUMYEqSkXJR1ttFJiFVYZphTg74zOkGTI8oljFOhQ+B3w0a91EbDab153K2sgw5Eoz3/ucAzDrirv/BfwIuAP4c2d7i7qjlHGBKkpFyaStdi42gfYh3jJGab4n63zWTcFaozjRiroCnHMf7/MR4PlZV9x9JzYf668721tSBTifopQEpVgBKEpxaKutwaZRSyvFJeTJ6FJiPOuzbjLQhTgikbJCZ5qZDrzX+7w064q7bwNu7Wxv+VOBz6soRUcVpTJ+aKuNACux8xiuAPZl9I4l9rMoJwFbwrWTa0ScYl7XFOAS4JJZV9z9FPBd4Dud7S2PF1EGRSkYqiiVsY21Gt8EvMVb1gYr0IjRx6KsnLckgg0Uej1cO2lyMCIBMBf4OPDxWVfc/Uvg2s72lp8HKI+iDBtVlMrYo612GtZqPAEbxRkNVqAR53XaNm7JWlcLpABC1Q2F6J8cCquB1bOuuPsx4AtYK3NnwDIpyqBRRamMDdpq9wDOBk4EFmPnHByr+LldawEDEKqsLTWreT/gm8BnZ11x91eAGzrbW17vp4yilAyqKJXRS1utAxwDnG+MebOIhIIWqUj4BfLU4TUOnPKaUlOUaaYAnwY+OuuKu28Brutsb3kqWJEUpX9UUSqjj7baycA7jTHvFpG9AETGsgG5G34WZT1eYJJTVlUqrtdcVGKjZdd4Q0yu7Wxv+X3AMilKTlRRKqODtloBVmGtxxNEJDLOlGMmfhblFGyyAaSsslQtymwcbD/yCbOuuPuPwEc721vuC1gmRdkNVZRKaWOjVt9tjDlfRObDuLMe/cifbCBSPloUZSZLgF/NuuLuu4HLO9tb/hW0QIqSRhWlUpq01VYDFxtjPiAiDaoc++BnUU4CupzK2nIJhUdzlG8LcOysK+7+BvCJzvaWV4IWSFFG62BrZazSVltFW+2HU8asAz4jIg1Bi1SC9LEoK+ctcYAGoCtcN6XU+ycHQgg7C8pT3ryaihIoalEqpUFbbQVwYcqYKxyRRkctyFzsALKtrGpsozcVrpkwGt2uuejGTv2lKIGiilIJlrbacmBNT8p8JOTIJFWQ/fIcbRuzZ+2oI51soLJuLCnKNh1vqZQCqiiVYGirDQPn96TMlSFHpoQcVZADJFeyATuGssIdC65XTE/yCQmFbwhaDkUBVZRKELTVrkimzI1hR/ZWBTlo/AJ5akmPoSyvGhsWpeNc2NnekgxaDEUBVZRKMWmrnba923ylIiInhlVBDpVcs4YkAZzRM4YyJya5855115z4y6DlUJQ0qiiVwtNWG9qRNB8IO7RVRKQiaHFGOX4W5VS8MZQSqRjVitKYVFLC0YuClkNRMlFFqRSUnk+4zTt7+E5FRPYJWpYxgp9FORnoknA0JOFodbEFGlFSPV/p/Pzxmv9VKSlUUSqFoa22YlOXuaY6ypqKiOh43ZEjex5KASYCr4XrptaO5sQMJtXzuoQinwhaDkXJRhWlMuJs/oi7IuzwXbdMpgYtyxjDAM9lrSsHyoBk2J04qt2uwIc621s2By2EomSjilIZOdpqnZe2pK6eVCWXOqJWZAF4ibaN2RMf907YXFU/aoeGmJ7utRKKfDPfPrGO2ALgYuBja89Z+1pxJFMUTWGnjBB/X1O956tbU3+bUu18QJVkwcg1hhIAp/QmbB4wEkckxjUAACAASURBVIpc0Nnekp1IIZvrsKntnoh1xM6PdcT0OVOKgj5oyrB57L3Vp85rdP4xscqJBS3LGCeXovTGUFaPSkVpkt0/7GxvecBvm9vsVrjN7lvnXz3/HcDR3uoG4Ebgj7GO2MHFklMZv6jrVRkyay+oDlVF5eYFE50zndEcRTJ68Bsa0pj+4pSNvmQDJpXqknDk/Xl2WS0hOTVcHfZLjr4YeCjWEbsJ+MDac9ZuKYyUynhHLUplSPxtTfXcKdXy79n1zlmqJIuGn0W5awylE60YfX2UJvX5zvaW7AAlANxmdyLwloZVDY2hqpCb4wgCvAd4JNYRW1woMZXxjSpKZdD888Lqd+w9wXl0YpUzN2hZxhl+FuVkoAtAIuW5lElJYnqSL0ko/Fm/bW6zK8BJ4dpwWVVT1fIBHG4u8GCsI/bhWEdMG27KiKKKUhkwrU0R518XVt+0zwTnm+VhzbATALnS1+0IuZOqxXFCxRZoWIhzaWd7y/YcW+cBSxuPatxXwlI2wCNGgHbg3lhHbNqIyKgoqKJUBsglS6K17avLfrPPxNB56mkNjOxkA2FsMM/OcO2kUdU/aZLdD6+7+vjv+W1zm90QcGbF7Ipo2R5lBwzh8EcCj8Y6Ym8ZlpCK4qGKUumXT6wom3vxkrK/LJgYOjRoWcYxm2jbuCFrnYtNQmDC1Y2jpn/SGGMkHFmTZ5elwMz6FfXLZeitskbgR7GO2A2xjph6P5RhoYpSycsXjy1fdsHi6ANzGpw5Qcsyzsk1NMQAOFWjaMLmnuS3O9tb/uq3yW12q4HTapfU1kdqIzNG4GxrgIdjHTEduqQMGVWUSk5uOr7i5HMPiP58ao0zKWhZFN9Anjq8CZtDo2QMpUn1bJVw5IN5djlOolLlLnJXjuBp9wX+FOuIXTyCx1TGEaoold1obYrId95a8YEz9o98u65caoKWRwH8Lco6epMNjA7XqzGf6mxvecVvk9vsTgWOazyycbZT5ox0BG858KVYR+y7sY7YQIODFAVQRalk0doUCb+rOXLdKftGrqqMDDjaUCk8fhblFGAngERLfx5K05NcJ6HwdX7bvOEgp0QaI5HKuZVLCyjGqcA9sY7Y6GhYKCWBKkplF61NkYrzD4zccnxT+OJISEbXUIOxT655KNPJBkpeUeI47+tsb8lO6p5mAbCo8ajGZglJoTOGrQAeiHXEZhb4PMoYQRWlAkBrU6TujFik47h54dM1005JkjPZgFNeHZVQpLzYAg0Gk+y+f91Vx//Eb5vb7EaAsyubKsvLppTtWySRFgB/iHXEFhbpfMooRhWlQmtTZNKJe4dvPnlB+CRVkiVLH4vSm7C5EdgRrptS0m5EY0yPhCPvzbPLYQiT6g+tP6xoQlmmAb+LdcSOKvJ5lVGGKspxTmtTpPG4ueGvnr0w0hpydHqsEqUbeDFrXRV2UoNUqKbEJ2zuSX69s73lX36b3Ga3Fnhb3fK6yeGacBATfdcAd8c6YucEcG5llKAV4zimtSlSt3p26H/OWxR5iyrJkuZ52jamstbVsWvC5tIdQ2lSPRslHPlYnl2Odyqcypr9aw4vmlC7EwFuiXXEPh6gDEoJo5XjOKW1KeKu2DN03ZrF0ZMjhQ+eUIZH3gmbQxVuKbter+xsb3nDb4Pb7M4EVjce1TjPiTpVRZbLj0/GOmJfj3XENJBN6YMqynFIa1OketmM0OcvOjh6ejQkkaDlUfrFL5Cn5CdsNj3dT4gTusFvmzcc5LTolGi4YlZFKU2+/G7gTk17p2SiinKc0doUqTxoWugzlyyJnlMWlmjQ8igDws+inIjnenXKKktSUeKELuhsb+nJsfUAYEHjkY0HiVNyQ5HeBPxfrCOmnhYFUEU5rmhtipTvVScfef8h0fMqNJnAaMLPotw1YXMpJhswye6frrvq+Pv8trnNbhlwZnWsuio6MTq/yKINlDcDN+vclgqoohw3tDZFopURLvrQ8rLza8qkMmh5lEGRK9lAF07IkXBZSaUZNCbVLeHIRXl2WYVDY90hdUEG8AyEM4EvBS2EEjyqKMcBrU2REHDeh5eXnb+H60wMWh5l0PhZlBOBHeG6qe4wpqIqDKmeL3W2tzzjt8ltdhuAExtWNkwLVYVGw7P4vlhHrC1oIZRgUUU5PnjzuQdEzm2eGpobtCDKkMiesLkMO46yO+yW1hhK05NcL6FIIs8uJ4ZqQmVV+1QVO7nAcIjHOmLvC1oIJThUUY5xWpsii1bsGbrwhL3DBwYtizIkXqFt4/asdbWkx1BWN+w2NCS1Ywuv3vFZ/nvTGv570xq6/us71p+uF59g3dWtbP337wHofu15XrzlEl745kW7yphUDy9/72OkuncMTFqRyzvbW7b4bXKb3TnAYY1HNS5wIk5Jp9zz4UuxjtiZQQuhBINGdY1hWpsiM2bXy4cuPDh6qCOaUGCUkmtoiAEIVdbuZlG+/quvUz77QCae+FFMTzemu2u3A5hUD2/cfwvlezXvWrf5bz+jbsW5hGsnseE3HUw8cR82P/JTqvZdhTOAVLKmp/vvEop0+G1zm10HOL18Rnm0fEb5aGy0CTa4Z+Pac9b65qxVxi5aeY5RWpsibk2UD1x5eNnq8rDomLDRS65kA94Yypo+ijLVtY0dz/2D6v2PBkBCEZzy6t0OsPkvd1HVtIxQZa9BKqEwJrkTk+wCJ0Rqxxa2P/UnqvZb1a+QxhgjociazvYWk2OXg4C5DasaDim5PtWBE8YOG1kRtCBKcVFFOQZpbYqEBd5z5eFlb5lQ6TQGLY8yLPwsyob0l+wxlMkNLxGqdHntp1/khZsv5rWffZnUzr5u0+Tm9Wx78g9UH3Bcn/U1i1rY9PAdvHbP9dQuPYUND3yX2qWnMCC91pO8vbO95SG/TW6zWwmc4R7o1kbqI3v1f7CSphybkGBR0IIoxUMV5RijtSkiwMlrFkdO32diaFbQ8ijDxs+inAp0ATjRyj59lCbVw86Xnqam+U1Me8eXkUgZmx76fp/Cb/zqJupXnIs4fcf5h91JTDm9nalnXYtEyujZ8jqRxumsv+taXv3xVXS//l9fAU0qtUPCkUvzXMPREhbXXeyW+nCQgeICP4t1xKYHLYhSHFRRjj2WLprqnHnM3LDOszc2yDkPJYBEy93MDeGaCYRqJlA2rQmAyqbl7Hz56T6Fu156ilfvvJrnb3gn2x5/gNfvvYFtT/yhzz4bfvst6g47k01/+QlVC1ZSd+jpbHjgVn8JTaq9s73FV4u6ze4k4PiGVQ0zQxWh+oFc8ChhEnB7rCOm2a3GARrMM4ZobYrMLgvxnouXlC3R4J0xQ65kAztC1Y2V4oT65OoNVdcTdifQ/drzRBqns2Pd34lMmNmn8PQ1/7vr+/q7r6NizkFUzl+6a92OZ9cSqm4g0rCHDQQSAXH8g4J6ki9IKHyVn+BePte3hevD0aqmquWDuObRwhLgy8CaoAVRCotWpmOE1qZIJXDhpUuj+zVUyISg5VFGjOwxlCHsFFtd4dpJvmMoG1avYf1d1/DCNy9i5yvP4C49hc2P/JTNj/y035MZY9j44G3ULj8NgJqFx7LhNx28+qPP4R781t0LOKFLOttbco0dmQ8c3Li6MSahMZtX+PxYR+wdQQuhFBYxJleQmjJa8Polz14+I/S2y5dH3+SM3qhCpS/baNvYZ/qpynlL6oBrgecq9z5sn+p9jzglGNHAJLsfWnfNCUv9trnNbhhoq5hTMWfimyeeOsYfyR3A8rXnrP1r0IIohUEtyrHBvlURjr7goOgyVZJjilxDQ7wxlMFN2GyMMRKO5HM5LgWmNxzecOg4eCTLgR/EOmKlPC+oMgxUUY5yWpsiNcB7Ll9etq9bJmMpWELxD+Spww5+x6moCS59XU+yo7O95e9+m9xmtxo4tfaQ2sZwbXi8RIbOAm4KWgilMKiiHMV4LtfTjtwrNG/R1JBGuY49+kk2UBWIBWNSPVskHLk8zy4tTplT7Ta7421g/smxjth7ghZCGXlUUY5umuvKOeK8RdFlQQuiFAQ/i3IK0A3gRAOasNmYts72lvV+m9xmdxpwTMPqhr2cMqekpv8qEl+MdcT2DVoIZWRRRTlKaW2K1AHnXb6sbL+qqLj9FlBGIzmHhgA4AUzYbHqSz0go/GW/bd5wkFMjEyORytmVvkE+44AK4HuxjpimjRxDqKIchXgu17MO3iM0db9Jzn5By6MUjJzJBiRaEZFwtPgTcDvORZ3tLd05tu4H7N+4unGRhGQ8j9HeD7gmaCGUkUMV5ehkKXDQeYsiB46DiMLxTB+LsnLeEqF3wubiW5PJ7vvWXXW872BMt9mNAmdV7V1VWTa5bEGRRStFLoh1xMarVT3mUEU5yvCiXM96+77h2inVzoyg5VEKRg+QnRauAogAPWF3QlEVpTEmKeHIe/PscjjCxLpD60bThMyFRIAbYh2xUL97KiWPKsrRx5vKw1S8Ze/IeIsoHG+8QNvGZNa6OtITNlfWF9ei7Ene2Nne8rjfJrfZrQVOrj+sfkq4OjylqHKVNguB9wUthDJ8VFGOIlqbIlOBY9Ysjs6sjkpwY+iUYpBraAgATqVbtKEhJtWzQcKRj+fZ5S1OpVNRvV/1WJkdZCT5ZKwjNi1oIZThoYpylOAF8LxtarWED50ZGosJppW++AXy7BpDGSqvLmZD6SOd7S0b/Da4ze6ewBETjpow34k6xQ8uKn1qgOuCFkIZHqooRw9NwIEXHRzdNzp2E0wrvfhZlBPw0tdJWVVRFKXp6f63OKGv+21zm10HOK1sWllZ+Z7lBxdDnlHKKbGO2FFBC6EMHVWUo4DWpkgIOLN5ihPad5LTHLQ8SlHwsyinUuwxlE5oTWd7SyrH1gOAfRpWNSwWR6d164frYx2xsqCFUIaGPtyjg0OAGe8+MLpUk56PG3IlG+hCRCRSVvAkEybZfee6q47/jd82t9ktB86qWVhTHZ0QnVdoWcYA84APBy2EMjRUUZY43jyTp66eHYpOd53ZQcujFA0/i9KOoaydXCPiFPTdNSa1U8KRi/PsciQh6mqX1GoAz8D5SKwjNidoIZTBo4qy9DkaqDph78jioAVRikp2soEI4AI7w7WTC+92TfVc19ne4mfV4ja7jcAJDSsbpocqQzpJ+MApB74StBDK4FFFWcK0NkUagTcfONVJzqx15gYtj1I0Xqdt45asdbWkx1BWNxR0aIjpSb4iocin8uxyUtgNl1XtU3VoIeUYoxwb64i9NWghlMGhirK0OQLglH0jS4IWRCkquYaG2AmbK2oLa1GK88HO9patfpvcZncusLzxqMYFTtgpL6gcY5dPxjpiGmswilBFWaK0NkWqgaPn1Mu2+Y2a+HyckSvZQMEnbDbJ7r+K43zbb5vb7IaAM8r3LI+WTS9bVCgZxgH7AicELYQycFRRli5LgfAZ+0cXhzT0frzhZ1HWk56wuUBjKI0xRsKRNZ3tLSbHLgcBsxtWNhwiGn09XD4WtADKwBlyBSwi00XkxyLypIg8LSJfEukdCC8i3xWRR0XkUhHZW0T+JiKPiMgcEXlwuIKLyGQRuUtE/i4i/xQR31kNhnmOlSJyl/e9VUSuGOlz+NHaFIkCrY0Vsmn/yc6BxTinUlL4WZRTgC4AKassTB9lT/K2zvaWh/02uc1uJXC6e5BbG6mPzCrI+ccXB8Y6YscELYQyMIakKL3W5A+BHxlj5gHzgWrgM972KcAyY8z+xpjrsG6GHxtjmo0xTxtjlo2A7J8E7jXGLDTGLAAKqsSMMXcaY9oLeY4MDgSqz14Y2U+z8IxL8icbiJSPuEVpUqntEo5clmeXYyUite6BribjHzmuDFoAZWAM1aJcBewwxtwMYIzpAS4F3ikilcAvgEmeFRkH3g+cJyK/BhCRXRF9IvIhEVnrWYbt3ro5IvJzEfmLiPxORPb2kWEq8Hz6hzHmUa/sLivQ+/0VETnX+94pIleJyJ+8z1xv/S0icqN3ridE5M3ZJxORc0XkK973iSLyAxF52Pss99av8K45bT3XDPbGell4TigPs3HJ9JAG8YxP/CzKSUCXU1lbLqHwyDeeTOqzne0tL/ptcpvdyUBLw6qGmaHyUNGSsY8DDo11xHQc6ihgqLOQ7wv8JXOFMWaTiDwLzAVagbuMMQfALgt0izGmz6zfInIc1tpcYozZJiIN3qavA2uMMU+KyBLgq1jlnMn1wG0ichHwS+BmY8wLA5B9kzHmYBE5G/gikFaKs4AVwBzg12klmoMvAdcZY34vIjOBe4B9gA8CFxpjHhCRajwLYJAsACaduX+ksTIi1UMor4x++liUlfOWOEAD8EK4dsrEkT6Z6Uk+L6Hw5/22uc2uAKeE68ORqvlVmox/5LkSO1ZaKWGGalEKXqj6ANfnYjVWwW0DMMa87imYZcD3ReRvwNew1mMfjDH3ALOBm4C9gUdEZCCVyHczlpkzkP+fMSZljHkS+I93zHxyf8WT707A9azHB4AviMjFQJ0xJns+wbx4M4S0AluWzwhpkunxSRfwcta6auy7mgrXNI68Rec4F3e2t3Tl2Lo3sHjCURMWSkgiI35u5ahYR+ygoIVQ8jNURfkPoE+mGBFxgRnA04M4jp9idYANxpgDMj77+BU2xrxujLnVGHMW8DBwOJCk73Vlj/UyA/ju9ztbxqUZ8u1hjNns9WGeh52J/qEcLuN8zAbmLp0eijRWOpMHWVYZGzxL28bsZ6832UDVyE7YbJLdD6y76vg7/La5zW4YOKtyXmV5dGp0/5E8r9IHjYAtcYaqKH8FVHruS0QkBFwL3JK2DgfIL+jt10REGowxm4BnRORt3joRkYXZBUVkVUa5GqzL9Fls/84CESkTkVrgyKyib89Y/iFj/dtExBGROViF5Tube4bcF2XIknYxzzHGrDXGXAX8mfxWqR/HAF3HzA0fMMhyytjBL5CnjgKMoTTGpCQcuSDPLocC0+oPq1+uo0EKSmusIxYLWgglN0NSlMYYA5yIVS5PAk9g++M+Osjj/Bzruvyz58b8oLfpDOBdIvJ3rPX6Fp/iB3rlHsUqvG8YYx42xjwH/B/wKPAd4JGscmUi8kfgEmwAUprHgd8AP8P2j+brX7wYWOwNf/knsMZb/34RecyTe7t3rAHR2hSpBRaXh1m/YKKjrffxS65kA3YMZXn1yLlee5Lf7GxvWeu3yW12a4BT6pbVTQi74T1G7JyKH8Ig606luIjVeeMDEekEFhtj1metvwUbfHR7EHIBtDZFVgJnn7JvuOrM/aOnBCWHEjhttG1MZK6onLfkrcBxwH8bj734vFBV3bAVl0n1bBYntFdne8trftvdZvc0p9w5do937HGiU+YMOnpbGTQpYM7ac9Z2Bi2Isjua8aUE8IJ4jgLeWD4jvJubWRlX5Eo2sANARmrCZmM+kUdJ7gEc3bi6cY4qyaLhAGcGLYTiz7hSlMaYWdnWpLf+3CCtSWAmMG1CpXTPrM07LEUZ+/j1UU4BuiQcDUk4OuwhQ6Yn+bSEwr7TPXnDQU6LTopGKmZXHDLccymD4qygBVD8GVeKsoQ5BEgePz+8d8iRUNDCKIGSPQ+lABOAHeG6qbUjElTjOO/tbG/JNXQpBsQaVzceKPosFpv5sY6YJhkpQVRRBkxrUyQMHAasXzwtpLOEjG8M8FzWujLsEKdk2J04bLerSXbfu+6q43/ht81tdqPAWVULqiqik6KDjdhWRga1KksQVZTBMxeonFYjoT1c2StoYZRAeYm2jTuz1tUxQmMojUklJRy5MM8uK3GYWLesTtOqBcepsY6YJnYoMVRRBs/BQLJlXngfR3Q6rXFOrqEhADiVtcMbGpLqub6zveVJv01us1sHnFR/WP2UcHVYk10ERyM2wlkpIbRiDhBvOq1lwKsLJobmBC2PEjh+gTyZYyiHbFGaVM8bEop8Is8uJ4SqQuXV+1UfNtRzKCPG2UELoPRFFWWwzAeiYYfkdHW7Kv4WZXqigOFO2PzhzvaWTX4b3GZ3FrCy8ajGvZ2IUzmMcygjw5tjHTGdpaWEUEUZLM1A97IZoWllYcnOSauMP/wsymmk56Ec4hhK09P9D3FC/+u3zW12HeCMsj3KouUzyxf77aMUnTJAk46UEKooA8JLMnAg8MZB00Kzg5ZHKQn8LMrJ2BlFkCFO2CyhyJrO9pZUjs2LgPkNqxoOFkf7yEsIjX4tIfTFCI5JgAvsmNfoaP+kAv4W5SRgR8idWC2OM+hxjSbZfUdne8vv/ba5zW45cEbNATU10caoPoOlxfJYR0y7Y0oEVZTBMQfALSMyuUqmBy2MUhJkJxsIY4N5doZrJw/amjQm1SXhyCV5dllNiLraJbUrBntspeAIdnIIpQRQRRkci4DtK2eF99RsPAqwibaNG7LWudgkBCZcPYQJm1OpazrbW7ITGNgDN7sTgBMaj2icEaoINfjtowROS9ACKBZVlAHgZePZD3jjgCnaP6kAuYeGGACnsnZQFqXpSb4sofBn8+xyUrg2HK3au+rQwRxXKSoHafRraaCKMhimAxEgObu+tPsne1KG5q9t4c232vm4z/jhNpq+soX9vrqFd/54O909/tO0fejeHez71S3sc/0WLv7ZDowxdCUNx357K/t9dQtffbg3Ac17frKdR17sKcr1lDC5kg0IQGiwEzaLc1lne4vvJOpuszsPWNZ4VOO+EpaywQqqFI0Qu088rwSAKspgmAvIDFeqGipkUtDC5ONLf9zJPhN6H5MzYhH+fWEVay+oYnvS8I2/du9W5sHnkjzwXA+PrqnisQuqePiFHn6zrod7nk5y4NQQj15Qxdf/YhXl31/qIWWgeeq49z77WZR1eO+olA082YBJdj+87urjb/Xb5ja7IeDMilkV0bI9ypqHJKlSTI4OWgBFFWVQHARsWjojNDNoQfLx/KYUdz+Z5LxF0V3r3jQvgoggIhw8LcTzm3YfdSDAjqRhZw909UB3j2FylRBxYHsSkhlFPv7rLj55hBo15J6HcieAU1YxIBecMcZIOHJBnl0OAfasX1m/TEZkKhKlwKiiLAFUURaZ1qZIBTAP2DSrzinpnJrv//kOrl5djuNTnXb3GL71aDfHzg3vtm3pjDBHzAoz9drNTL12M8fMCbPPxBBHzQnz0pYUS76xlQ8tL+POx7s5cGqIaTX6GJJ7HkqbbCAywGQDPclbO9tb/uK3yW12q4DTag+ubYjURUq6kabsYlasI6Zz1AbM7rWcUmj2xAZopKbVlK6ivOuJbiZVCQdOC3F/5+5TF7737h0cvmeYw/bc/RF66vUU/1qf4vnLagA46lvb+O26JIfvGebWk2yGtO4ewzHf3sadp1Vy2T07eHZjirMXRmhtGrcTJ+RMNuCUV0clHOk3c5NJpbZJOPKBPLscJ1GpcRe5OjvI6OII4KmghRjPaFO++EzHC9CYUCklqygfeLaHOx9PMuuLmzn19u3c90ySM3+4HYDE/V28us3whWP8XaZ3/KubQ/YIUR0VqqPCcXPDPPR832Cdrz68k3MWRvjDcz1EQ3DbyRV8+rddBb+uEsZvwuZGYEe4dsrArEmT+nRne8vLfpvcZncK8KbGIxtnOeXOsOe1VIqKRiYHjCrK4jMH2O6WEamJUh+0MLn43Opynr+shs731/C9kytYtVeYb7+1gm/8dSf3PJ3kuydV4OTo4ppZ6/CbdUmSKUN3j+E365J9AoLe2G6468kkZy+MsK3b4AiIwI7dDdfxQjfwYta6KqzHJxVyJ/TbP2l6ks9KKHyt3za32RXg7ZHGSLRybuXSYUurFBud0SVgVFEWn9nA1uYpocmjMZZizV07eHlriqX/u5UDbtzCJ39jrcA/v9DDeXdai/PkBWHm1DvEbtjKwhu3snByiOMzXKqf/E0XVx5WhohwzNwwf36hh9gNW3l3RtDQOON52jZmR0XVMpgJmx3nfZ3tLdmTPqfZB1jUuLpxoYRk3Pq2RzF7xTpiewQtxHhG+yiLSGtTpAyYCDw3v7F0+yezWTkrzMpZ9lFJfsL13WfxtBDfaK0AIOQIXzu+Iufxrju2t7utPCz84qyqEZR2VJJraAgAoQo3r6I0ye7frrvmhDv9trnNbgQ4q3J+ZXnZ1LL9hiemEiCHArcFLcR4RS3K4jIJLyXZdNcp6fGTSlHJlWwgPWFzTterMaZHwpH35jn2ocDU+sPq1X03utH/L0BUURaXyXiBPFOqSzeQRyk6fhblRDzXqxOtzG1R9iS/0dne8g+/TW6z6wJvr1teNzFcE546EoIqgbEkaAHGM6ooi8tMvMqvoUIVpbKLXMkGdgBImf8YSpPq2SThyEfyHPd4p8KpqFlYo8NBRj9NQQswnlFFWVzmAlvm1ItbFpZ+x8Up44ZcyQa6cEKOhMtqcpS7srO95Q2/DW6zOwNY3bi6ca4TdapHSlAlMGpiHTH1CgSEKsoi0doUEWAWsHWvekdnBFAy8bMoJwA7wnVTXb9Uc6an+0lxQl/1O5g3HOTU6JRopGKvCnXZjR3mBy3AeEUVZfGoBcqB7gmVoi18JZM+FmXlvCVlQDXQHXYn+vdPOqELOttbck25shDYr/HIxsWic52OJdT9GhCqKIvHruCMhgpVlMouXqVt4/asdb1jKKsbdlOUJtn983VXHf8rv4O5zW4ZcFb1ftVV0YlRrVjHFmpRBoQqyuJRgxfxWlumilLZRa6hIQYgVFnbx01vTKpbwpGL8hxvJQ6NdUvrNIBn7KENn4DQhAPFoxqvYeKqolR68Qvk2TVhs1OeNQ9lqufLnZ8//mm/A7nNbj1wUsOKhqmhqtDEkRZUCRy1KANCLcri0QgkAaqjqiiVXfhZlPWkFWVZ1S5FaVI9r0ko0pbnWCeGqkPlVQuqdHD62GR2rCOmKQgDQBVl8WjEm4S3KkqucH9l/OFnUU4DumC3ZAMf6mxv2eJ3ELfZnQ0c3nhU2IKgSwAAIABJREFU495OxMmdP1AZzYSxuaKVIqOKsng04CnKyohalMoucs5DCSDR8loA09O9VpzQzX4HcJtdBzijfHp5tHxm+eKCSaqUAup+DQBVlMWjAdjpCFIepjJoYZSSwc+inATsCFU3VIoTigBIKHJ+Z3uLyXGMxcDchlUNS/zGXCpjCg3oCQBVlMWjDtg5rUYqHRG970qa7AmbQ9g+yq6wO2kCgEl2397Z3vIHv8Jus1sBnFGzqMaNNETULTf2UYsyALTCLgKtTZEoUAb0TKmWcT+nlLKLbbRtXJ+1Lt1/bZwKd5ZJpbokHLk0zzGOlrDU1h5Uu6JAMiqlxYygBRiPqKIsDtV4A8grwqJDcpQ0uYaGGKAmVNPoYFJXd7a3PO9X2G12JwKtDasaZoYqQvWFFFQpGTQQMABUURaHarwB5I7oPVd2kSvZgAATIg17PCyh8Of8Cnr5XN8WrgtHq+ZXLS+kkEpJoYoyALTSLg67gnccQYMtlDR+FmUdduaQfznl1Z/tbG/JTm+XZj6wpPGoxv0kLNGCSaiUGhoxHwCqKIvDrvscclRRKrvINTRkK/Dd5750Wq4ptELAmRWzK8rKppUdUEgBlZJDLcoAUEVZHIR0phW1KJVe/CzKicBd2578o58STbMUmFG/on6ZjgYZd6iiDABVlMVhV22mQ0OUDPyU4e3AHbkKuM1uNXBa7SG1DZHaiEZAjj/KYx0xDQgsMnrDi4OQng1CLUrF0gU8nr1y25N/fKWfcsdJVKrcZleHg4xfagBft7xSGNS6KQ677rO6XhWPT9G28eXBFHCb3anAcY2rG2c7ZY5bILmU0kcDeoqMKsrikNlHqfd8nJMy5jHg6sGU8YaDnBqZEIlWzqlcWhjJlFGC9lMWGXW9FoeMPkq1KMczKWNSxvAOEhu7B1l0X+CAxtWNB0hIk1aMc1RRFhm1borDrvusQYrjm01dfCP0yU1/HkwZt9mNAGdV7V1VXjalbN8CiaaMHlRRFhlVlMVhl+t1y07TFbAsSkBs7zYv1ZXL+4dQ9HCEyXXL6w4fcaGU0YgqyiKjirI47LIjX99ucmVaUcY4yRTn0rZxUP+/2+zWAqfUr6ifFq4JTymQaMroQuvtIqM3vDgY78OrW822gGVRAmDDDvP9ms9tumcIRVsjjRG3Zr8aHQ6ipNkctADjDVWUxWE7nqJ8ZatalOONrqTZUFcu7xlsObfZ3RM4csJxExZrPlclgy1BCzDeUEVZHHZZkduT9HT3mMFGPCqjmK4e1tC2ccNgyrjNbhh4Z+3BtVOjE6JzCySaMjpRi7LIqKIsDn2syK4e1P06Tti4w9zrfm7TbUMoemSoJjTfPcg9dMSFUkY7qiiLjCrK4rCNjICeHUl1v44HdvaYbeVhzh5sObfZnQK8beJxE2NOxKnst4Ay3lBFWWRUURaH7WTc6x1JtSjHA9u6+VDZpze9NJgybrPrAOdWx6qnlk3TMZOKL9pHWWRUURaBOx/v7ga6gRDA9m61KMc6m7vMw3Xtm64fQtHlTrkTqz+0Xl2uih/da89Zq2Oxi4wqyuKxGS9l4LZuVFGOYZIps7M8zNsHW85tdhuAMyccO2FvTXqu5EDdrgGgirJ4bAYiAJt3mq0By6IUkC07+XTkU5ueGUwZL+n5mZXzKqeU71m+qECiKaMfdbsGgCrK4rEJT1G+uNm8FrAsSoHYstP8u65cPjuEooskLAc3HNGwXDQhsJIbtSgDQBVl8diI53r9zxup9QHLohSAnpTpcYRTadvYM5hybrNbA7yj8ejGOaHKUGOBxFPGBqooA0AVZfF4FSgDWPtKz3pjTMDiKCPN5p38T+VnNv19MGU8l+sp5TPKp1bOrTy4QKIpYwd1vQaAKsri8SLe/d7URffWbjYGLI8ygmzrNs/VlcuHh1B0HxxWNB7VeIg4ou+j0h+vBC3AeERfzOLxKl6+V4A3tht1v44RUsaYlOEM2jbuHEw5t9mtAN7VcETDnmE3PK1A4ilji/8ELcB4RBVl8VhPRnaeV7epohwrbOriW9Wf3fS7IRR9S3RSdGb1guplIy6UMlZRRRkAqiiLx1Zshp4IwAubU68GK44yEuxImvV15XLhYMu5ze4c4NgJx05YLCEJF0A0ZWyiijIAVFEWiTsf7zbA80AlQOcGjXwdC3T38C7aNg4qwMJtdqPAO+uW1U2PNERmFUYyZYzydNACjEdUURaXZ/AU5T9fVUU52tm4w9xZ87lNdw6h6NHhuvDcmkU1y0dcKGUs0wX8N2ghxiOqKIvLc0AU4PlNZmuXziIyaulKms215fLOwZZzm93pwFsnHDdhoRN2ygsgmjJ2eWbtOWt1XFkAqKIsLuuBVPrHa9uNhnqPUnYkuZi2jYPKsOQ2uyHgHTWLaqaVTS5rKpBoytjln0ELMF5RRVlc+gTwPPNGal1QgihDZ1OX+W1t+6ZbhlB0RagqtKDukDp1uSpD4R9BCzBeUUVZXDZgLcoQwKMvpzoDlUYZNN09Zkd5mDMGW85tdicCp004bsICJ+pUF0A0ZeyjijIgVFEWkTsf705hA3pqAH7/bPL5npRJ5S+llBJbu7ky+qlNzw+mjDcZ81lV+1RNKZ9evn+BRFPGPqooA0IVZfF5BHABNu+k+9VtRqPYRgmbu8zf68rlC0MoerBEZVH9Cp2MWRkySeCJoIUYr6iiLD5Pk5HKrnOD9lOOBnpSJhkJcSptGwcVdeg2u3XA2ROOmTA/VB6qK5B4ytjnqbXnrB1UikRl5FBFWXye9ZYOwFrtpxwVbN7J1eWf3vTvwZTxZgY5tWKviqkVsysWF0g0ZXzwx6AFGM+ooiwydz7evYOMfsrfrks+lzLaT1nKbN1pnq4rl/gQiu5PiGUNRzYsE52NWRkevw5agPGMKspg+BteP+XGLnau32ZeDFgeJQdeI+Z02jYmB1PObXargHc2rm6cE64OTyqMdMo4QhVlgKiiDIanMn90bjDaT1mibOri61Wf3fSnIRQ9qWxa2R5VTVVLRlwoZbzxn7XnrH22/92UQqGKMhjSilEAHnulpzM4UZRcbO82L9aVy2WDLec2u00IRzYe03iwOBIqhGzKuOK+oAUY76iiDIA7H+/ejg3qqQG475lkZzJlBuXaUwqLMeb/t3fn8XHV9f7HX9/ZM0lOppl0py3QQCn7sAkUWSoiKBa9XpVFqFAf7v68jx/3IT+X37UKQq/LDxWvGyIICqKCElYR2Sm10AYYWpjuCylt0jSZk21mzpzz/f1xZtp0Ie0MmZ5J8nnyyCOZM/M980lJ+873nO+CrbmKhemS1uM1EkYEWDDu7HHTgw3BaRUqT4wtctnVYxKU3mkFGgDMLNbmtJbtc6pIOsu9dTeaT5TR9EPBeHBG/fH1shmzGC4SlB6ToPTO6sEPlr9tv+FVIWJ3mbzuikXU50ptZySMGcDFTRc1naz8KlSB0sTYk0rOT8pgP49JUHpnHWADAYBH1+RTspxddcjm+TwL0+lS2hgJIwgsaHhPw9RQU2hmhUoTY4/cn6wCEpQeaUlZWWA50AjQ3qczW3r0em+rEumMfrxhkfmnMpq+z2/4jzBOMWSZOjGc5LJrFQh4XcAY9y/gtOKD1q32ymkNPumNeCRn6/5IgKtKbWckjMnAx8dfNP54X9BXU4HSRq3UtSl8NT6UUuCH5oXN5HvzbP7FZqztFsGmINO/OB1/7d6Dh7feu5WeV3tAQ+0xtUy+YjI6r9n0k01YXRaNcxuJvy8OQNvtbTTObaRmxoj636OBp70uQkiP0msp3G23fAAtqfxK29G2tyWNXQMW14ZvMLeV0qawM8j8uuPrJocnh4+uUGmj2mHXHUbz9c00L2wGYPvD26mbXceR/30kdbPr6Hi4Y682/av76V/dT/MNzTR/r5mB9QP0vdlH7+u91BxaQ/P1zXQ93QXAwKYB0Iy0kARYkZyf3PubFwedBKWHWlJWP/Aagy6/bkzr1UO3EpXQk9X/alhk/rKMpmf5anzHj5szTjZjHiZmq0nsLHf9+NhZMczl5t4vUuBYDjqv0ZZG25pAQwDlV+5xZ9fa9e33tzPhoyNycaRyRl2LCpBLr957ATix+GDJW/nk4eNCR3lYz5iTd3QuEuCyUtsZCSMOXNF0YdNRvrDPqEBpo5+CDT/cAEDjeY00nttIPp0nGAsCEIwFyZt7TzGONkepnV3Lm19116mPvy9OZEqE8MQw3Yu7WffddTR9sAmz1aTm0BqC44IH7VsaRn/0ugDhkqD03krc0a9+wG5J5Vf9+9HBbMivwh7XNWb05vhubJFZ0kCqws4gV0SPjE6KTI8kKlTaqHf4Nw8nOM4Nww0/2EB48oH92Ge3ZcluyTLr5lkAbPjBBupSddTOqmXa5911HnRes+FHG5j+1em8fc/bWJ0WsTkxjMSI+J1mVXJ+UnYMqRJy6dVjhVV6XgLGA/Rb5Fd1Oiu9rWrs6M3plbGIuqmMpiergDq18dzGObIxSPmKPb2AEaD+pHoG1g0QaAhgdVsAWN0WAWPv3+fNZSbRmVH8ET/+iJ/64+vpX9u/22s6n+wkNifGwJoBlF8x7YvT6GgZMbf87vK6ALGLBGV1eAHYOUG9JZUvZxFuUSJHa9unuIyF6ZLmrxoJwwA+Hb8gfoQ/6o9XqLxRz8k62AP2zq97V/QSnhrGONGg+/luALqf795nDzAUD9GX6kPbGp3X9L3Zt1tv1O6z6Xm1h9icGE7O2fkvnWNV/1RlrbUGfu91HWIXufRaHVYBGdywzC15y966pcfZOKXeN8PjukY1M8tPYovM10ppU7jk+onI9MiUaHP01AqVNibk03k23eJuiqFtTcPpDdQfX0/N4TVs/p/NdD3XRbAxyLQvuZdSB9YPsOOpHUy9ZirGqQa9b/Sy5ltrQEHdcXW7BWr7A+1M+PAElFLUHVtH5z87WfOtNTSe1+jJ91oKpdTzyfnJDV7XIXZR7i8vwmvzZgU/DlwAtAF8/OjAUVeeEPqkt1WNXv2W3hQNqiNYmM6V0s5IGMfg47qpV089P1AfmFyp+sSY9tnk/OStXhchdpFLr9XjWdwevgK47418qieru70taXRytNaO5ooyQjIKLGg8r/FQCUlRCVrrLPBnr+sQu5OgrBItKWsb7o4iEwAcjV7yli33KivAzHJH3Y3m82U0nReaGJpWd3TdGcNelBCAUurB5Pyk/IJcZSQoq8vfgUjxwd1Ja7ll65J6PWJombzuiEXUV0ptZySMmcCFTRc2nar8Su7ti0q50+sCxN4kKKvLauBtwADoHNDZFR3Oq96WNLrkbK5hYbqvlDZGwggBn4nNiU0LjgvKACtRKduBx7wuQuxNgrKKtKQsB3gQGFc89peV1r9kwNXwSGf0A8ZN5kNlNP1AYFzgMCNhyDJ1opL+mJyftLwuQuxNgrL6LAcGgDDAa9uczk2y/uu7ls1rsyGiFpTazkgYhwAfbbqoKaECslqSqChZZKBKSVBWmcI+lY9SGNQD8Mjq/IveVTQ6ZPJ8hYXpzlLaGAnDD1xtnGRMCU8IH1mh0oQAeD45PymD96qUBGV1egF3mogP4NE1+fVtpiObOpfJzOpnGhaZ5QySONdf65/dcHqDbMYsKu17Xhcg3pkEZRVqSVk7gCUM6lX+IWk9IfcqS2fZOhMJcEWp7YyEMQG4tOmipmN9IV9tBUoTAgCt9fLk/KQM4qliEpTVqzhVxAfw/CZ7y9ouWSy9VP0W3whdb7aV0qawGfOVtUfXTo4cEjmuQqUJAYBSSnqTVU6Cskq1pKyNwIvAxOKx25Zb/3S0rv5VnatET1a/0hBRPy6j6em+sO/kcWfLZsyisrTWbwB/9boOMTQJyur2NyCIu1clKzqcHcltznJvSxoZbEfng34+ycJ0SderjYQRA66MfyB+hD/ij1WoPCEAUErdmJyflHsqVU6CsooVlrX7B7BzXdFfL8s9bdla5lrtR0+ORZEbzFWltCnsDHJZzcyaSTWH1ZxcodKEAEBrvR64x+s6xP5JUFa/RwGHwn6Vm03dt7TNlukiQ+jL6TWxiPpOGU1PwM8ZjXMbz1SyG7OoMKXUouT8pO11HWL/JCirXEvK6gZagEnFY79elnshk9f979xq7HK0djRcxsJ0vpR2RsKoA66Jnx+fGagNTNhvAyHeBa31FuAOr+sQB0aCcmR4EugHagC6MuSe3mA/621J1cnM8su6G82Xy2j6sfDU8JTaWbXvGfaihNiDUur7yflJ2fBghJCgHAFaUlY/8BcGzav8zfLcS10DusO7qqrPgKW3xCLq2lLbGQljFoq58Qvi71E+5a9EbUIUaa23A7Ix8wgiQTlyvAB0AvUAORvnttbcA46sQgCA1hpbcxUL05lS2hkJIwJ8Ztw542YEG4KHVKg8IXZSSv0gOT8pt05GEAnKEaIlZVnA3UBT8dizG+22ZVucJd5VVT3SWf5Yd6P5zzKafijYFJxef1z9mcNelBB70I5eD/zE6zpEaSQoR5ZXgBUMGthz85Lsk2ZW7/CuJO9l8npHLKI+X2o7I2EcCny46aKmU5RfBYe/MiF2p3zqfyXnJ7Ne1yFKI0E5ghT2q/wdEKCwDVdvjvydr+ZaxvIV2JzN51iYTpfSxkgYQWBBw3sapoTiocMrVJoQOzmW82RyfrKc/VCFxyQoR5jCIgT3AFOKxx5fa29MtjvljPQc8dIZ/Zhxk/mXMpqeHzACRxinGLIziKg47ei8L+gr+aqHqA4SlCPT08AaYHzxwI8WZ//Rm9OmZxV5IGfrvnCA+aW2MxLGZODfmy5qOt4X9NVUoDQhdqNtfUtyflI2YB+hJChHoJaUZQO/xZ1XGQR3buUfX7ce9LSwg6zf4trIDWZ7KW0KmzF/uv6E+knhyeHZFSpNiJ10Xm/zBX3/1+s6RPkkKEeolpTVBtwHTN11LL/mjQ77Ve+qOnh6snpJbJH5qzKanuWr8R0XOzP23mEvSoh9+0xyfrLP6yJE+SQoR7bHgc0MmjLyoxdzj/XmdEkDW0aavKNzkQCXltrOSBhx4PKmC5uO8oV99RUoTYjd2Bn74dcXvF7SAB6lVFwp9UrhY6tSqm3Q41AJ57lBKfUfpVe9z3P9Xin1keE410gkQTmCFeZW/gaoxR0JS3ufzvz8pdyfbEeP2sWWe3MsDF5vbiylTWFnkE9FZ0UnRaZHEhUqTYiddF73+SP+BSW307pTa32i1vpE4JfAzcXHWmtZ9s4DEpQjXGGD5wcZdAn2+U32lkdW5x/1rqrK6c3pFbGI+u8ymp6igurUxnMaz5KNQcTB4OSd65Lzk9uG85xKqflKqaWF3uXPlVK+wvEPKaWWK6VeVUo9PqjJcUqpZ5RS65RSXyq8tlkp9bpS6jal1Aql1KNKqUjhuZOUUv9SSr2mlLpPKdWwjxreX3j/pFLq1mIvVyk1TymVUko9p5S6RSn1N6WUXym1RinVWHiNv1BL43D+uVSaBOXo8DCwEZhYPHDrcmvZinb7Fe9KGn62o+2gj0tZmHZKaWckDAP4dPyCeLM/6h9Rf0HFyGRn7Jf9Ef/Ph/OcSqljgY8CZxZ6mwHgUqXUJOAXwEe11ifAbrcljgTeD5wOfFepnWsZzwJ+rLU+BhgAipdVfw9cq7U+HkgBuw1CUkpFcQcSfkxrfRwQBT5bOP5z4ALgbAqLomitbdzpbJcXTvEB4CWtR9YiKRKUo0BLysri/pAC1BWPX/9s9uHt/c5Wb6oafmaWm8M3mK+X0qZwyfUTkRmRKdGZ0VMrVJoQOzmW06MC6pLk/ORwrwJyPnAq8LJS6hXgHGAmcAbwlNZ6I8AeIfSQ1jqntW4HdrBrStkarXWy8PUy4FClVByIaK2fLxz/HW7oDTYbWK21Xlt4fGfhNUcDKa31Ru2ufjJ4Q+rbYOc0rmuA28v79r0jQTlKtKSsduB/cP8iBAD6LfLffyF3bzavS1oovBr1W3rjuBr1zTKaHoOPs+Pnx09XPiU/76KitNY6n85/esWCFVsqcHoF/HbQ/cpZWuvrC8ffKZQHL5dnU/i34R2OH8g9iXd6zTu21VpvALqUUucBCdxBiCOK/MMxirSkrNdxt+OaVjz25nan+/evWfeP5CXuHK21o7mChemSBjIYCSMKLGic23hooD4wab8NhHiXcu25O1PXpu6v0OmfAD6hlGqCnaNjp+PuLDRXKTWjcLys2wuF7b8GlFLFDQKuBJ7Z42UrgSOUUsVlHz9VeM0KYJZSappyBwF8co92twF/AP6otS7p1kk1kKAcfR4BWhk0uOeBVH714s32nj/wI4aZ5fa6G80Xymh6SWhSaFrd7Lozhr0oIfZgpa03B9YPlDzK9UAVLpV+B3hCKfUabs9sotZ6G/AF4AGl1Ku4gVSuK4GbC+c/Grhhjxr6gQXA/UqpJG7P9NbC8S/jhvlzwBZg8DS1vwINwB3vojbPqJHc0xD7Nm9WsB74NhDCvS+BT6F+elHk8ukNvmZPiyvRgKXba4LqcBamS5qwbSSMZuBbU+ZPOTc4LjijQuUJAYCTdfoymzPHrr1+7Qava/GKUqpOa91b6FH+CkhqrW8pPHc6cJPW+jxPiyyT9ChHoZaU1QPcgju/MgLgaPR/PZX9y0gb3GM5XF1GSIaABbGzYtMkJEWlaUfr7Nbs1WM5JAu+UBhktBJ3ec1bAZRS3wTuBb7hYW3vivQoR7F5s4JzgM8BGwAH4BBD1d70vsg1DZHqn8eUzui/Niwy/63UdkbCuCQwLnD5lCumXKICKlyJ2oQoyr6dvXXV/1n1Wa/rEJUjPcrRbTHuPYPpxQNvmbrv+mezd/bldI93Ze1fNq/Nhoj6TKntjIQxDbhk/AfHnyghKSrN6raSAxsHPud1HaKyJChHsZaUVZzP9AqDwnJVp5P+4eLsXdm8HvCsuP3I2nyZhemSJiUbCSMAXG2cYkwJjQ8dWaHShADAzthmblvuos2/2CyX5UY5CcpRrrAe7C+B1QwaCbvsbafjZ0tzd1u2tjwr7h2YWf2UcZN5VxlNz/XX+Y9qOK1BNmMWFaUd7eS25j617sZ1bV7XIipPgnIMaElZGdzBPVspLC0F8MxG+63bX7HuraYF1C1bD0QCfKrUdkbCmABc2nRR07G+kK+2AqUJAYDWmsymzA1rvr1mTO3/OpZJUI4RLSmrF/h/gMmuZax4aFV+7Z9W5P/qVMmorj6Lr4euN0ta1cRIGD7gqrpj6iZGpkaOq1BpQgDQv7r/7va/tS/0ug5x8EhQjiEtKasL+BHuklU7R73e87q14pHV+Yc9K6ygJ6tbYxH10zKanu4L+xKx98pmzKKy+lb1Pbf9ke0LzFazKn6xFAeHBOUY05KytgE/AIKAUTz+62XWsgdT1kNe9SxtR+eDfi5lYbqk9zcSxjjgyviF8SP9Ef9eWwIJMVz61/W/sv2R7f9mtpojfu1kURoJyjGoJWVtxu1ZGriLEgDu1lz3JK0/e3HPsifHTZEbzFWltCnsDHJ5zcyaKTWH1pxcodKEIPNWZtX2R7Z/yGw1t3tdizj4JCjHqJaUtQb4MdDEoLC8d0X+jV8ts/6Qsw/eTup9Ob06FlHfKaPpCSqgzojPjZ+hZDdmUSHZbdlN2x/b/sH0S+lK7AgiRgAJyjGssNvIj4BxuAsWA/DYmvz6m1/M3ZHJ6/5K1+Bo7fgUl7IwXVIv1kgYdcA18fPjh/tr/eP320CIMuQ6c9s6n+j8cNdzXWv3/2oxWklQjnGFsLwJd03YePH4C5vtt7/7TPa2nqzuruT7m1l+UfM9c3kZTT8WnhqeGj0yetqwFyUEYKWtHTue2vGxzsc7X/O6FuEtCUpBS8pai7udTh6YWDz+eruz45tPZn67Y0C3V+J9+y3dFouo/yy1nZEwjkIxt+mCptOUT/krUZsY2/K9+Z6up7qu6niwo5zt3cQoI0EpAGhJWW3Ajbh7yE0uHt/QrXu+9o/M7Vt7nc3D+X5aa2yHK1mYLmkEoZEwIsCCceeMmx5oCBwynDUJAWD3271dz3R9Ydtft3k+ZUpUBwlKsVNLyurAvQzbBkwrHm/v05lr/565a80Oe+VwvVc6yx/qbzKfKqPpxcHxwRn1x9XPGa5ahCiyuq3Ojoc6vty/uv9ur2sR1UOCUuymJWWlgR8CbwAzAAXQk8P633/P/vnxtfm/24523s17ZPJ6RyyivlhqOyNhHApc3HRh08nKr4LvpgYh9pTdmm3b9pdtX8tuyd4pCwqIwSQoxV5aUlY/8FNgKXAYsPM+4M+W5pbcsjR3R79V/jZdOZvPsjBtltLGSBhBYEHD6Q1TQ/HQ4eW+txD70r+uf/XWP2/9L7vX/p2EpNiTBKXYp5aUlQN+DTyI27OMFp97cr29+T8fz/yqzXQ2lHredEY/atxk3ldGSe8PGIEjjJMNueQqhlVPsueVjpaO67C5w2w1q2aDAFE9VJWshS2q2LxZwQTwBcACOorHAz7U1+aE5r5nqv+sA5nvn7N1r6M5PHKD2bHfFw9iJIwpwPWTLp10RnhSeHaJ5QuxT9rRTnpJ+sX00vQ3gOekJyneiQSlOCDzZgUnA18CpgCbgZ0/OB+bHZh16bHBj4QDKjLUOdIZ/dmGReatpbyvkTD8wHX1J9af1Xhu40VllC7EXnRe5zqf7Hyyb2Xf18xWM+l1PaK6yaVXcUBaUtbbuHMtF+PetwwXn7vvjXzq209nf93Z72x7p/Y9Wf1iqSFZ8F5f1Hds7IyYbMYshoWTdfo7Huq4v29l3xclJMWBkKAUB6ywAfRthY+JuEvfAbCyw+n60iOZ3yxtsxfvuQNJ3tHZSIDLSn0/I2E0AZc3Xdg02xf21b/L8oUg35vv3nbftjsHNgz8h9lqrve6HjEyyKVXUZZ5s4KHAV/G3YGkbfBz58zwH7LgpNAlsYhqAujO6K/HFpmLSjl/YWeQr0ZnRec2Xdj0YVnzXLxb2be1ayxDAAAJPUlEQVSzGzse6bjL7rF/YLaaJY26FmObBKUo27xZQQNYAJwIbAGyxeeiQQJfOCV0yUmT/XZ9WJ3EwnRJcy+NhHGaCqqvTL166gf9UX/j/lsIsW/a0bbZai7rfq77LuA3sp+kKJUEpXhX5s0K+oFzgctwR8UW71NOBNZfNyd085zf9lmlnNNIGAZw0/iLx58SbZZFz0X57AG7a/tj2xdnNmbuBu6V6R+iHBKUYljMmxWcBFwNHAVsx92261stKWtrKecpXHL9TOTQyEUTLpnwEdlnUpQruyW7pv3B9hedAec24FmZ/iHKFfC6ADE6tKSsrfNmBb8PnANcAfyp1JAsOAYfZ8fPl82YRXl0XufSL6eXppekFwM/M1vNYV3QX4w9EpRi2LSkLBt4ct6s4ItAyfeBjIQRBRbE58ZnBOoCk4a9QDHqWV3W5o5HOl62OqxHgLvNVrPim4+L0U+CUgy7lpQ1UGbTj4QmhQ6pnV17xrAWJEY97Wi7d0Xv0h1P7liJ5nZgsVxqFcNFglJUBSNhNAMXxOfGj1N+JT+X4oDle/PtnX/vXJLZnFkO3Gq2mlu8rkmMLjKYR3jOSBhh4DtATaAhkIlfEH9/eEo4IbcoxVAcyxnofa13SdcLXZtxuB94xGw1SxphLcSBkKAUnjMSxiXAR4CNxWN1x9TNiJ0Zu9hf62/yrjJRjbSjncymzMud/+hcbffZW4Bfmq3mOq/rEqOXBKXwnJEwvo47rWQzkC8eV0Hlj78vfmb0iOjZcjlWAFid1trOJzuXZtuyOeAJ4D6z1Sz3nrgQB0SCUnjOSBgR4EJgHu5o2fbBz4cnh2Ox98bODU8OHy9TRsYme8DekV6afqantacHWAX8wWw1N3hclhgjJChF1TASxlTgKtze5VZgt55CZFokHpsTOzc0MXSs5OXYoPM62/dm3/M7nt7RpvO6C/g9sNxsNUtaElGId0OCUlQVI2H4gDNwFy0IA28z6HIsQM2hNRNiZ8bODY4PzpbAHJ201jrbln2l8x+dr+fT+RzwAPCEXGYVXpCgFFWpsN7rBbiXZMHtYe4emDNrJsXOiJ0XagodebDrE5WhHe3k2nMru5d0JzMbMjlgCe59yA6vaxNjlwSlqGpGwmgEPgCcD2jcHuZuC1tHZ0Wnxk6LnReMB2d6UKIYBjqvc5nNmeXdL3a/mmvPRYBNuJdZV8vCAcJrEpRiRChs4vxB3J1K8rg9zN3uU9UeUzu94dSGucFYcMbBr1CUw8k6Pf1r+//V/UL363afHQP6gHuAJbLTh6gWEpRiRDESxgTgYuC9QA53W6/dA/Oo2kPqjqs7OTwpfIzyq6AHZYr9yPfmt/W90bc4vSS9Udu6GJCPAk+brWafx+UJsRsJSjEiGQljMvBh3IE/Odwe5m4/zP5af9g41Tg2OjN6UqA+MMWDMsUecp25tb2v9S7uebUnDdTj/qLzALDMbDWzQ7cWwhsSlGJEMxLGIcAlwCm4l2Q7cINzNzUzaybVn1B/UnhK+DhfwBc5yGWOaY7lZHLbcivNZeZLA+sHFO5o5hTwILBSpnqIaidBKUaFQmDOwb2HGQF6gC726GX6wr6AcYpxdPSI6ElyL7NynLyTybXnUv1r+lf0vta7Sef1BEDhjmJ9HNgog3TESCFBKUaVwgLrxwLvB47EDcoO9rE/ZuSQSLz+pPqTIodEjveFfHUHt9LRR+d1NteeS/Wv7V/R81rPWm3pCBDH7ek/jnv/cbu3VQpROglKMWoZCWMScDru1JJaoB/Yzh69THAvzUabo83hyeHmgBGYpnzKd3CrHZl0XudyHYVwfLVnjbZ0GDccFe6f9ePAizJAR4xkEpRi1DMSRhCYDcwFji8c3o4bnHvxRX2humPqDq+ZXtMcHB9s9kf8DQep1BHBsZx+q9NatzMcczrErnDcATwDvAK8JZdXxWggQSnGFCNhxIFTcVf9KQZgL5Bmj2kmRZHpkabokW5vMxgLzhhrO5k4OafP6rI25LbmNvav79+Q2ZDpAGpww9GHey+4GI6bJRzFaCNBKcakwpqyk3HvY55a+Kxww3IHeyzIXuQL+wK1s2tnhKeEpwXHBScHjMAkX9hnHKy6K0072rH77fZ8V74t15FrG1g/sCmzOdNZeHpwOHYDzwKtwCYJRzGaSVAKARgJowY4HHcg0GlADDc4+3BD4R1XiQnEAtGaQ2smhyaGJgfHBSf66/xN/hp/UzX3PLXWaEv3OgNOt91vd+U6c1uybdm2gXUDbztZp7imbg3un0Nx0YYu4AVgOW44yrQOMSZIUAqxByNhKGAC0Izb2zwGtxcFbnD2ANaQJ1Go8KRwQ2hyaHwoHmoKNASafGFfrQqpqC/oq1EBFVVBVVPJ/TWdnNPnZNwgtPvs7nxPvjvfne+2Oq3u7LZsWuf04EXmfUAdYOD+gqCATuBVYCWwEdghPUcxFklQCrEfRsIIAYfhBueRwEzc3ha4gdKPG6AZ9jGidij+en8kUB+o8df7o/6ov8Yf9Ud9Nb6oL+yr8YV9NWi0drSNja0dnde2tnGwtftfvvDZfT6v807eyee78z25bbnuQT3DPQVw55rWAaFCzRo3DFcCawtfd0swCiFBKUTJCj3OGDAJmIobnjOA8ewKSoUbnBnceYRW4fPB+AtXDMLih49dA5V8hZragXXAKqAN2Gq2mkP3koUYoyQohRgmhWkocaAJNzQPAybirmlajzuXE3b14Ip8uMFqFT504bFv0OfBX7OP8+hB5yoG4VZgC+6CC92DPjLSUxTiwElQCnGQFEbaRoAo7qXbwZ9rcXupBu7l0GJo5vb4OofbM7UHfeRxR+lKEApRARKUQgghxBBkmS4hhBBiCBKUQgghxBAkKIUQQoghSFAKIYQQQ5CgFEIIIYYgQSmEEEIMQYJSCCGEGIIEpRBCCDEECUohhBBiCBKUQgghxBAkKIUQQoghSFAKIYQQQ5CgFEIIIYYgQSmEEEIMQYJSCCGEGIIEpRBCCDEECUohhBBiCBKUQgghxBAkKIUQQoghSFAKIYQQQ5CgFEIIIYYgQSmEEEIMQYJSCCGEGIIEpRBCCDEECUohhBBiCBKUQgghxBAkKIUQQoghSFAKIYQQQ5CgFEIIIYYgQSmEEEIMQYJSCCGEGIIEpRBCCDGE/w8/Th7P+qH4dAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 576x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = data['Category'].unique()\n",
    "plt.figure(figsize=(8,6))\n",
    "plt.pie(cat['Profit'],autopct='%1.1f%%',labels=labels,explode=(0.05,0.05,0.05),shadow=True,startangle=60)\n",
    "plt.title('Distribution of Profits Categorywise',size=25,color = 'green')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TOP 10 PROFITABLE SELLING ITEMS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sub-Category</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Copiers</td>\n",
       "      <td>55617.8249</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Phones</td>\n",
       "      <td>44515.7306</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Accessories</td>\n",
       "      <td>41936.6357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Paper</td>\n",
       "      <td>34053.5693</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Binders</td>\n",
       "      <td>30221.7633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Chairs</td>\n",
       "      <td>26590.1663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Storage</td>\n",
       "      <td>21278.8264</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Appliances</td>\n",
       "      <td>18138.0054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Furnishings</td>\n",
       "      <td>13059.1436</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Envelopes</td>\n",
       "      <td>6964.1767</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Sub-Category      Profit\n",
       "0      Copiers  55617.8249\n",
       "1       Phones  44515.7306\n",
       "2  Accessories  41936.6357\n",
       "3        Paper  34053.5693\n",
       "4      Binders  30221.7633\n",
       "5       Chairs  26590.1663\n",
       "6      Storage  21278.8264\n",
       "7   Appliances  18138.0054\n",
       "8  Furnishings  13059.1436\n",
       "9    Envelopes   6964.1767"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dftop10_items = data.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values(by='Profit',ascending=False)\n",
    "dftop10_items.reset_index(drop=True,inplace=True)\n",
    "dftop10_items=dftop10_items.head(10)\n",
    "dftop10_items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 6.800000000000036, 'Products')"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 972x648 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot('Sub-Category','Profit',data=dftop10_items,kind='bar',aspect=1.5,height=9,palette='ch:2.5,-.2,dark=.3')\n",
    "plt.title('Top 10 profitable products',size=25,color = 'Green')\n",
    "plt.xticks(size=15)\n",
    "plt.yticks(size=15)\n",
    "plt.ylabel('Cumulative profit',size=18)\n",
    "plt.xlabel('Products',size=18)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TOP 10 PROFITABLE CITIES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>City</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>329</th>\n",
       "      <td>New York City</td>\n",
       "      <td>62036.9837</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>266</th>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>30440.7579</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>452</th>\n",
       "      <td>Seattle</td>\n",
       "      <td>29156.0967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>438</th>\n",
       "      <td>San Francisco</td>\n",
       "      <td>17507.3854</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>123</th>\n",
       "      <td>Detroit</td>\n",
       "      <td>13181.7908</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>233</th>\n",
       "      <td>Lafayette</td>\n",
       "      <td>10018.3876</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>215</th>\n",
       "      <td>Jackson</td>\n",
       "      <td>7581.6828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Atlanta</td>\n",
       "      <td>6993.6629</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>300</th>\n",
       "      <td>Minneapolis</td>\n",
       "      <td>6824.5846</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>437</th>\n",
       "      <td>San Diego</td>\n",
       "      <td>6377.1960</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              City      Profit\n",
       "329  New York City  62036.9837\n",
       "266    Los Angeles  30440.7579\n",
       "452        Seattle  29156.0967\n",
       "438  San Francisco  17507.3854\n",
       "123        Detroit  13181.7908\n",
       "233      Lafayette  10018.3876\n",
       "215        Jackson   7581.6828\n",
       "21         Atlanta   6993.6629\n",
       "300    Minneapolis   6824.5846\n",
       "437      San Diego   6377.1960"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city = data.groupby('City')['Profit'].sum().reset_index().sort_values(by = 'Profit',ascending = False)\n",
    "city.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 6.799999999999997, 'City')"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABJEAAAJeCAYAAAAEIJTpAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjAsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+17YcXAAAgAElEQVR4nOzdebgtZ1kn7N9DmBJIIIQwKWEIKpOKEgFRGUUGhSAtIg5MdgM2iIIf3YAMYVBAGZtgQ75mvhoj3QIaNfARpogMEpFBQpghyBw48ZCJDDzfH1WLs9jZe9de56ydvc/Z931d61q7qt5617tqDddZv/PWU9XdAQAAAID1XG6rBwAAAADA9idEAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQC4TFXVm6uqq+pF+9DH2WMf913m2PYXVfXh8fn/4V7uf6tx/66qqy97fPuTqrpiVf1xVX2sqs6bOy53Grfv07HewONffe4xb7VJj/Ez4+fu61V18fhY7xq33XdcPnszHhuAA8vlt3oAALC3qqr3YfeHdverlzWWzVJVP57kZ5P89Hj7iSRXSvIf3b3hH/9V9VtJfnfc/ypJvpzkLUme291fWva491ZVPTLJdZK8pbvfv9Xj2R9V1ROSXDnJid19xlaPZz/wiiS/Pf59QZKvj39fOLXj/nCsq+qWSU7NMM5OsivJRUm+vZXjAmD/JEQCYH/29TXWXzVDULJem/OXP5xN8bokP7m3O1fVQUlOTPJr46pLkpyX5Ogkj0ryO1V17+4+dV8HuoB/T/LJrP7aPDLD8z07yXoh0qeSHJbkO0sf3f7h8xlCgdWCgCckuVqSDyfZlsHGdlFV10vyW+PiI7r7hFWabfaxviTD5yEZQqxle3SG8X8kyd27e63vRACYJEQCYL/V3ddZbX1VHZfkaeu12Y9clORjST403m6WIWjZqGdmCJAuSfLEJMd39/njDKfXJPmpJG+uqptdVj8uu/vRS+jjNssYy/6qu391q8dwgLhFksrwOftfqzXY7GPd3d9JctNNfIgfH+//rwAJgH0lRAKA7e123X3JbGGRuixV9UNJHjcuPq+7/3y2rbs/VlW/nOT0JIcneXKS31/OkGG/cch4f153f29LR7J5Zs/xnC0dBQAHBIW1ASBJVV2/ql5cVWeMxXW/U1UfqapnVdU11tjnB4oTV9WPV9Xrq+orVfXdqvr82OeRezuu+QBpLzwgQ/2ki5I8b5W+v5rk1ePiA6tqr/5zqaquVlVPqKp/qqpvjc/9zKp6e1U9pqqOWNH+UoW1q+oPxxpXs1P3Xjh3bC9VAHojhbWr6nZV9dqq+kJVXVBVu6vqX6rqKVV1tXX2u0NV/dX4HL5bVeeMr+U7quqJVXXtBY7Ns8ZxnrLG9q+N28+tqiuusv2vxu3/Y8X6SxV7rqoXjcdw9tzetOL4rVk4uaqOqqqXVdUXx+f8lfHY3Wijz3VFfz9QrLmqfr6q/mYs7HxBVX2yqp5ZVVddY/8/HPf/8Lh8r6r6+3H/S2pFUfaqukJV/V5VnVpV3x6fw5fGz+Nt1+o/yZvHVVdbcazePNd2qcd6lbGsWVh7le+YDb9Os89IklmfKz9TGy7iXQt+P1bVL27wfd1V9fOrbP+9cdtHNzpGAC4bQiQAdryquleSTyR5TJIfy3Dq10EZilD/cZLTq+qnJ7q5a5IPJHlghppMneSGY58frarNPF1lLXcb7z/Y3Wet0ebk8f6IJLde9AGq6ucy1Cd6dpLbZ/hRfW6SH05ylyQvTnLvDXR1boYaSRePy98Zl+dvG5opUlWXq6oXJHlfkt9JcoOx34MzFCd/RpIPV9WPrbLvY5K8O8mvJ7n++JiXZHgt75zkTzMUOt+od4z3t6+qK614rFskmQVShyS53YrtleRO4+I7N/BYuzMcp1nB+bNz6WO4mttkqOnziCSzQOC6GY7dP1fVj2zgsddUVb+T5F1J7pMh1Lxckh/NMPvtg1W17imnVfWUJH+f5F5JrpgV74OqumaSf0ryF0l+IcmhGep+/XCGz+P7q+rJK7qdvd9mYU/nB4/TromntbfHel8s+jrNxrHWZ+qijTzoXn4//lOS72b6fZ0M3xMrzdZt5H0PwGVIiATAjlZVP5rk/2QoxP2hJD/T3YeOy3dL8sUMP/RPqhUzalZ4RZKPJrlVdx827n+fDD/WrpPkjStDhMvALcf7f1unzfy2WyzS+RjCnJzkWkk+k+RXk1ylu6+R4fn/VIbQZXJWRnf/v2P9qo+Pq57a3ddZcdu9waE9NcljMxRCfmySa3X3VTOESLfPEC7dMMnfzs+SGF/f2Sl/L09yg+4+uLuvlqGI988meVGmA4Z5783wY/rgXDp8uvN4P3teK39M3yLDse0Mwda6uvup4zGc9ffQFcfvUqHZ6MQk/5LkJ8f3/lUzvHe/leSaSZ4/9djrOCTDsXxrkpuMVxS8apIHZwhybprkf4/BwmpukuTpSV6a5LrdfXiGY/ni5PuBxF8m+ZkMwdF/TnLo2O6oJG8Y+3lmVf3GrNO599tDx1W7Vxyr2fpV7cOx3hcLvU7d/WMTn6mPZ8Lefj929/kZQvVk7ff1qu/78TW947goRALYZoRIAOx0T8/wQ/crSe7a3aclSQ9OSfJLGa6YdL0MgcRazslw5aOPjPtf0t0nZfiR970MBbEftGnPYnXXHe+/vE6br2bPbIrrLdj/8zLM+vj3JLfv7jd393eT4Udkd3+4u/+4u9+8bi9LVFU3yDA74qIk9+ruF3X3N8cxXdzd78vwo/VTGWbD/Obc7rfOMNPl6939yO4+c7ahu7/T3e/v7sd292SgM7ffBRlCq+TSP6Znyy+a2P6R7t7My7F/NsOx+miSdPdF43t39n6/V1Udtpd9XyHDLJb7dvdnx/4v7O7XZgiSkuF5/uIa+18lyau6+9Hd/bVx/4u7+/Pj9l+a2/eh3f2K8Zinu7+UYSbS7FTC59RwtcL91Wa+TmvZl+/H2Sy8td7Xr8wQJN2uqg6e2/7jSY7M8L254c8aAJcNIRIAO9Y4C2VWU+fF3X2pGTPd/akkrx0XH7hOdy/q7v9YZf9/TvKWcfE3Vm7fLFV1SIZTTpJhhsaquruTnD8uHrpA/9dK8svj4tNnQc028JAMFw55V3d/YLUGY8gwm6Fy97lNs9f/4Jqrv7QEs9kU3/8xPTfb4pIMIdJ/JLnt+LrN3HnF/pvlud292qlNfzveH5QFZ6mt8OzV+u/uv85Q2D1Z/7Px7HW2PWC8P72737By41gs+6nj4g0yzETbX2326/QDlvD9OHvfrvW+fluSUzOc4vhzq2z/SHcvMusPgMuAEAmAneyWSa48/r1q4ePR28b7G1fV4Wu0ecca6+e3HbPA2La7n81wafQkOWkrB7LCrEjvz9VQtHrVW5I/GNvdYG7fjyb5UoZT1/65qh5bVbesqn3999Ls9b9NVV1l/PtWGeranDb+UD41wyyon0+Guk657E7pWSts+48Mp5wle2rw7I19+Wx8o7s/s87+s/3evk6b92fPlcn258/gZr9OK+3r9+P7MwTYq72vL87wnr9UwBr1kAC2NSESADvZteb+Xu+Ur39fY5956+0/23bYZVUXqbvPyzDLJdlzie9LGWfEzE4l+c4CDzErhvzd7t6MIsJ7a3ZK3iEZarWsdTt0rl2S789QekCGU3d+JMkLknwsydlVdXJV/e5evn4fyPBj+goZCj8ne2ZbvGPF/ewH9K2SHJ7hNTx1Lx5zEeu97rOizFfYy74vmDgVb/bZWOtz9Y2J/mf7rfn5G2fbTT3O/mAzX6fV7NP3Y3dfmKEmWHLp9/UHu/ucrHjfjyHTHcZ1QiSAbUiIBACDnm6ybruN7n9Z+up4/0PrtLlu9swo+spePMZ2e96zU/ie0921gdsPXOZ8rJl0dIbTq16R5IwMBYzvkeR/Jfm3qrrJIgMaT0H6p3HxLivu1wqRZvcfWu00yf3Ivr4/LplustDjbLf36/5ib4/vyplGK9/3H8lQGPyYsZ7TTye5ei6b8BSAvSBEAmAnm5/lcP112v3w3N9r1f754TXWJ3tCnN2zwtOXkdmV1265Tpv5bZNXa5ozC6iuXFXXXrflZetr4/2P720H3X1Bd/9Vd//n7r5ZhqDtDzOcEnWTJCfsRbffD4nG4s6/kOGqbbNw6WNJzkry01V1tRw4p/QcXFXrnWI1+2xMzThay2y/NT+/42y72Qy17VK7a3+wjO/H2ft+5fv6Hcn3Z4m9O0P4e4e57f/SG78aIwCXISESADvZv2W4slCS3HWddrOrP312nUKvd15j/fy20xYY2zLMapX8zPzlt1e4x3j/7QyXD9+o92XPrIN778XY1vK98X6tS75P+f6Mn6o6cgnjSXd/vbtfnOFKVUlyx6pa9LShWRj0UxkujX5YkvePl0Kf/Zh+V4Yf03fNntpOexMi7esxXLb1Pht3Gu/39rMx22+9z+9ts+f0xQ/u5eOsZbsd62VaxvfjaRlOw5t/X1+QPae5JT84C++yKiYPwF4SIgGwY401O940Lv7BalfkqqqjkzxoXPzLdbr7g6q61NXNqurW2RPU/NU+DHdv/FWG2S5XSPJHKzeOM4geMi6+vrsvXtlmLePV2GYFtZ+2rMAmwyW/k+GUlr3xygz1YQ5O8uJxFsqqquqg+Uuib6De0ewqdp3FT4s6LcNzu1yS48Z1KwtOz344/7cMocfFSd6z4OMk+34Ml+0JVXX5lSur6r7ZMxNubz8bJ473N6uqX1/lMSp7jvcXM4Sfy7TdjvXSLOP7cfxO+cdxcfa+ft9Yf2xm9r7/pexbeArAZUCIBMBOd1yGosfXS3LKGPqkBnfNMJvn4Az1gl60Tj+HJXlrVf3EuP/lqupXkvxdhv+F/2T2XAp7w6rqylV1zdktyVX2bNqzfrz9QGDS3V/OUBw6Sf5bVf1RVV153PmWSf4+Q5HbXUmetejYkjw+wyyDH07y3qo6dhbEjOP+6ap6cVX96gJ9zk7BO7aqFi6C3N2fTfLMcfGBSf6uqm4zOzbj63LLqvrvGV6TO8zt/siqekdVPayqvn/Vtqq6QlXdJ8nTxlX/3yKB2ziuS7Lnx/Rtx/uVIdI7VmyfFR9e1OwY/sZqweZl7KIMl51/U1XdOBkuHV9Vv53kdWObd2XPrLlFvS17rhz2qvni51X1w0n+d5K7j9ufML4Oy7SdjvVmOC77/v04C4RWfd939+kZTkO9RYb6Yxdl78JTAC4Dl/pfIQDYSbr7U+MMhjckuXWS06pqdvrF7Mpd30hyn+7+1jpd/W6GH8UfqardGS5rPbs89jeS3G/F/75v1COTvHCV9Yfl0vVHDk9y9op1T0nyo0n+U5LnJXlOVZ037p8MMynuuzdXWBuP3b2SvDFDraA3J7l4PH5Xz55TfP51gW5fkeQRSX4yyVer6hsZZlMlyU9ssE7KMzP8G+fJSe413r5bVeckuVp+8N8/8zOKKsPpNHdOkqq6IMMP6Ktnz3+8fT7Jf13g+cx7R5JfHv8+Nysu2d7dZ1TVVzPUYEr2fjbGy8fH+aUk3x6P4UUZanL9xF72ubfOS/L7SV6V5Feq6uwMn6srjts/leS3xtP5FtbdXVW/meQfkhyTofj5/xxf6/nLzT+1u09crY99tJ2O9dIt6ftxrbB03rsyFLNPhvD03H0aOACbxkwkAHa87v77JDdL8pIkn85w+ldnmGXwp0lu3t1T9YLenuF/2k/MEBBcLsmZSY5P8uPj/7Zf5rr7ku7+tSS/nSGU2J3kSkk+l+Sl49j2+ipI3f2eJD+W5KkZ6s2cm+HH5ZcyHJPfT/K3C/T3rxl+kJ+coU7TkUluMN429O+WHjw1w6lSL01yeoYf9ldL8h9J3p/kT5L8zPjaz7w+ycMyhIEfy1BI+7AMx+y9Sf57hiDrCxt9PivMh0LvGa/atl6bvQqRuvukJL+W4Yf5d5JcJ8PxO2pv+ttX3f26DLWPTsrwOnSGz9mfJjmmu/fmqoDz/X8zye2TPCrDDJZzM8xo+XKGz+PPdvcz1+5hnx57Wx3rzbCE78cPZ5jtmAyfqX9epc18sORUNoBtrPbyP34AYMerqltlzyybw7t75Swg2JHGekdvSvIf3X3A1QsCgJ3KTCQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgEkKay/ZPe5xj37LW96y1cMAAAAA2Bu11gYzkZbsrLPO2uohAAAAACydEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmHT5rR7ATvbym91uq4dwQHrEJ96/1UMAAACAA46ZSAAAAABMEiIBAAAAMEmIBAAAAMAkIRIAAAAAk4RIAAAAAEwSIgEAAAAwSYgEAAAAwCQhEgAAAACThEgAAAAATBIiAQAAADBpS0Okqrp8VT2hqj5dVd+tqn+vqheuaFNV9aSq+lJVnV9Vp1bVrVbp6+ZV9faqOq+qvlJVz6iqgzarLwAAAICd5PJb/PivSnLXJE9PckaS6ye5+Yo2T0jylCSPH9s8LskpVXXL7v5aklTV4UlOSXJ6kmOTHJ3k+RlCsidvUl8AAAAAO8aWhUhVdY8kv5HkJ7v79DXaXDlD8PPs7j5+XPe+JF9I8ujsCXUemeTgJPfr7t1J3lZVhyU5rqr+rLt3L7OvZR4HAAAAgP3BVp7O9rAk71grQBrdPslhSd4wW9Hd5yY5Kck959rdM8lbVwQ8J2YIg+64CX0BAAAA7ChbGSLdNsmnqur4qto91h96Y1Vdb67NTZNckuTTK/b9xLhtvt0Z8w26+8wk5821W2ZfAAAAADvKVoZI10nykCS3ynBa20OT3DrJm6qqxjaHJzmnuy9Zse+uJIdU1RXn2p29ymPsGrctuy8AAACAHWUrC2vXeDu2u7+VJFX11STvTnKXJG8f2/Ua+67ctla7jbTZm772bKh6eJKHJ8lRRx21WhMAAACA/dpWzkTaleRjswBp9J4kF2bPFdp2JTm0qg5ase/Vk5zX3RfNtbv6Ko9xteyZVbTMvn5Ad5/Q3cd09zFHHnnkak0AAAAA9mtbGSJ9Yo31leR7499nJDkoyU1WtFlZt+iMrKhXVFXXT3KVuXbL7AsAAABgR9nKEOnvkvxEVV1zbt0dklwhyUfG5fcm2Z3k/rMGVXVIknsnOXluv5OT3L2qDp1b94Ak52c4PW7ZfQEAAADsKFsZIp2Q5FtJTqqqe1fVbyZ5XZJTuvs9SdLdFyR5TpInVdWjququSf5PhnG/ZK6vlyX5bpI3VtUvjjWKjkvygu7evey+AAAAAHaaLSus3d27q+ouSf5HkhMz1EL6mySPXdH0ORmCnicmOSLJaUnu1t1fn+tr1xgKHZ/kpAy1i16YIfzZrL4AAAAAdozqXvWCY+ylY445pk877bQNtX35zW63yaPZmR7xifdv9RAAAABgf1VrbdjK09kAAAAA2E8IkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElbGiJV1UOqqle5PXKuTVXVk6rqS1V1flWdWlW3WqWvm1fV26vqvKr6SlU9o6oOWtFmaX0BAAAA7CSX3+oBjO6S5Py55c/N/f2EJE9J8vgkZyR5XJJTquqW3f21JKmqw5OckuT0JMcmOTrJ8zOEZE/epL4AAAAAdoztEiJ9sLvPWbmyqq6cIfh5dncfP657X5IvJHl09oQ6j0xycJL7dffuJG+rqsOSHFdVf9bdu5fZ1/KfPgAAAMD2tt1rIt0+yWFJ3jBb0d3nJjkpyT3n2t0zyVtXBDwnZgiD7rgJfQEAAADsKNslRPpsVV1cVZ+sqkfMrb9pkkuSfHpF+0+M2+bbnTHfoLvPTHLeXLtl9gUAAACwo2z16WxfzVCj6J+THJTkgUleVlWHdPcLkxye5JzuvmTFfruSHFJVV+zuC8d2Z6/S/65xW5bc1w+oqocneXiSHHXUUes9XwAAAID90paGSN391iRvnVt1clVdKcmTq+rFs2ar7FqrbFur3Uba7E1fexp3n5DkhCQ55phjVm0DAAAAsD/bLqezzfu/Sa6R5IYZZv8cWlUHrWhz9STndfdF4/Kucd1KV8ueWUXL7AsAAABgR9mOIdJMZ6hNdFCSm6zYtrJu0RlZUa+oqq6f5Cpz7ZbZFwAAAMCOsh1DpP+U5KwkX0zy3iS7k9x/trGqDkly7yQnz+1zcpK7V9Whc+sekOT8JO8el5fZFwAAAMCOsqU1karqrzMU1f5ohllCDxhvj+nu7yW5oKqek+QpVbUrw0ygx2UIv14y19XLkjwmyRur6rlJbpzkuCQv6O7dSdLdS+sLAAAAYKfZ6quzfTLJw5JcP0Ph6tOTPKi7XzfX5jkZgp4nJjkiyWlJ7tbdX5816O5dVXXXJMcnOSlD7aIXZgh/skl9AQAAAOwY1e1iYst0zDHH9Gmnnbahti+/2e02eTQ70yM+8f6tHgIAAADsr2qtDduxJhIAAAAA24wQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmCZEAAAAAmCREAgAAAGCSEAkAAACASUIkAAAAACYJkQAAAACYJEQCAAAAYJIQCQAAAIBJQiQAAAAAJgmRAAAAAJgkRAIAAABgkhAJAAAAgElCJAAAAAAmbThEqqpXVtVt19l+m6p65XKGBQAAAMB2sshMpIckOXqd7TdK8uB9Gg0AAAAA29IyT2e7SpKLltgfAAAAANvE5dfbWFVHJbnh3KqbVtUdVml6jSS/l+QzyxsaAAAAANvFuiFSkocmeVqSHm9/PN5WqiTfG9sDAAAAcICZCpHenOQLGUKiVyY5Icn7VrTpJOck+WB3f2nZAwQAAABg660bInX3R5J8JEmq6gZJ/rq7/+2yGBgAAAAA28fUTKTv6+6nb+ZAAAAAANi+1gyRZgW0u/vU+eUps/YAAAAAHDjWm4n0riRdVQd394Wz5XXa17j9oKWNDgAAAIBtYb0QaXaltYvG+4dl/RAJAAAAgAPUeiHS55N8ors7Sbr71ZfJiAAAAADYdi63zrZ3JrnbbKGqPldV99msgVTVD1XVOVXVVXXVufVVVU+qqi9V1flVdWpV3WqV/W9eVW+vqvOq6itV9YyqOmhFm6X1BQAAALCTrBcifTfJleaWb5jkqqs3XYo/T3LOKuufkOQpSZ6b5N5jm1Oq6jqzBlV1eJJTMpxud2ySZyT5oyQrryi3zL4AAAAAdoz1Tmf7VJIHV9WHkuwa1x1RVUet12F3n7noIKrqF5LcI8mfZgiTZuuvnCH4eXZ3Hz+ue1+SLyR5dJInj00fmeTgJPfr7t1J3lZVhyU5rqr+rLt3L7OvRZ8fAAAAwP5uvZlIz0py+yQfylAfqZO8aPx7vdtCxtPEXpJhxs9ZKzbfPslhSd4wW9Hd5yY5Kck959rdM8lbVwQ8J2YIg+64CX0BAAAA7ChrzkTq7v9bVR9Jcqck103ytCRvTvLRJY/hkUmunOSlSX5rxbabJrkkyadXrP9EkgesaPeO+QbdfWZVnTduO2nJfQEAAADsKOudzpbu/nTG0KWqjkvy1939+mU9eFUdkeSZSX67uy+qqpVNDk9yTndfsmL9riSHVNUVu/vCsd3ZqzzErnHbsvta+TwenuThSXLUUeue7QcAAACwX1o3RJrX3eud+ra3/iTJB7r7H9Z76FXW1Srb1mq3kTZ709eext0nJDkhSY455phV2wAAAADszzYcIs1U1dEZrlp243HV55L8TXd/dsF+bpHkYUnuUFVXH1cfMt5fraouyTD759CqOmjFDKKrJzmvuy8al3eN61a6WvbMKlpmXwAAAAA7ykIhUlU9M8MVzg5asenPqupPu/upC3T3I0mukOR9q2z79ySvSPL68bFukuSTc9tvmuSMueUzxnXzY71+kqvMtTtjiX0BAAAA7CgbPkWtqh6W5I+TfCDJr2YIgX4kyX0zBJDP9BcAACAASURBVEF/XFUPXeCx35Pkzituzx233SvJnyd5b5LdSe4/N45Dktw7yclzfZ2c5O5VdejcugckOT/Ju8flZfYFAAAAsKMsMhPpURkCpDt198Vz6z9bVf+Q5B+TPDrJqzbSWXefleRd8+uq6objn//Y3eeM656T5ClVtSvDTKDHZQi/XjK368uSPCbJG6vquRlOtTsuyQu6e/f4eBcsqy8AAACAnWaREOlmSZ64IkBKknT3xVV1YpJnL21kezwnQ9DzxCRHJDktyd26++tzj7+rqu6a5PgkJ2WoXfTCDOHPZvUFAAAAsGMsEiJdmOSq62w/dGyz17r71UlevWJdZ7iK259M7Ht6krtMtFlaXwAAAAA7yYZrIiX5YJJHVNW1V26oqmsleXiG090AAAAAOMAsMhPpmUnenuQTVfWKJKeP62+R5KEZZiL91nKHBwAAAMB2sOEQqbtPrar7ZagV9EcrNp+Z5MHd/Y/LHBwAAAAA28MiM5HS3SdV1d8nuXWSGyWpJJ9N8qHu/t4mjA8AAACAbWBDIVJVXSXD7KMPdPdbM9RH+uBmDgwAAACA7WNDhbW7+9wkT0py/c0dDgAAAADb0SJXZ/tskuts1kAAAAAA2L4WCZH+Isl/qaojNmswAAAAAGxPixTW/k6Sbyf5ZFW9Jsmnk5y3slF3v3ZJYwMAAABgm1gkRHr13N+PXaNNJxEiAQAAABxgFgmR7rxpowAAAABgW9twiNTd797MgQAAAACwfS1SWPsHVNXBVXXwMgcDAAAAwPa0UIhUVdeqqr+oqq8kOSfJOVX11XHdtTdniAAAAABstQ2fzlZVN0ryniTXTfLJJO9PUklumuSRSY6tql/o7s9txkABAAAA2DqLFNZ+fpIjktyvu988v6GqfjXJXyZ5XpL7LW94AAAAAGwHi5zOdtckL10ZICVJd78pyf8c2wAAAABwgFkkROokn15n+6fGNgAAAAAcYBYJkd6d5M7rbL9Tknfty2AAAAAA2J4WCZH+MMltq+r5VXWt2crxim0vSHLbsQ0AAAAAB5hFCmu/PcnBGYKiP6yqszOcvnb4uP2sJO+oqvl9uruPXsZAAQAAANg6i4RIZ0bNIwAAAIAdacMhUnffaRPHAQAAAMA2tkhNJAAAAAB2KCESAAAAAJOESAAAAABMEiIBAAAAMEmIBAAAAMAkIRIAAAAAk4RIAAAAAExaKESqqkOr6qlV9Z6q+nRV/ey4/prj+ptuzjABAAAA2EqX32jDqjoyyXuS3DjJZ8b7g5Oku8+qqgcnuXqSx23COAEAAADYQhsOkZI8K8l1ktw2yZlJvrFi+98kueuSxgUAAADANrLI6Wy/kuQvuvtDSXqV7Z9Lcv2ljAoAAACAbWWREOmaGU5jW8v3klx534YDAAAAwHa0SIj0tSRHr7P9pzKc5gYAAADAAWaREOkfkvxuVV135Yaqum2SB2WoiwQAAADAAWaREOnpSS5O8q9Jnp2hLtKDq+ovk5ya5CtJnrv0EQIAAACw5TYcInX315LcLskHkjwsSSX5nSS/nuT/S/IL3f3tzRgkAAAAAFvr8os07u4vJTm2qg5L8mMZgqTPCI8AAAAADmwbDpGq6oju/laSdPfuJB/ctFEBAAAAsK0sUhPpK1X1xqo6tqoWmsEEAAAAwP5tkRDpjUnuPt5/tapeXFXHbM6wAAAAANhOFims/cAk10ny8CSnJ3l0kg9U1cer6vFVdb1NGiMAAAAAW2yRmUjp7u909yu6+45JbpzkuCRXSPLcJF+sqrcsf4gAAAAAbLWFQqR53f3F7n5md/9okt9Kcm6Suy1tZAAAAABsG3tdILuqDk1y/yQPSvLzGQKpf1vSuAAAAADYRhYKkaqqMhTXflCSY5McnOSbSY5P8pru/teljxAAAACALbfhEKmqnpfkN5NcO8lFSf4+yWuS/EN3X7w5wwMAAABgO1hkJtLjknwwybOS/GV379qcIQEAAACw3SwSIt28u8/YtJEAAAAAsG1t+OpsAiQAAACAnWvNmUhV9aDxz9d1d88tr6u7X7uUkQEAAACwbax3Oturk3SSE5NcOLdc6+zTSYRIAAAAAAeY9UKkOydJd184vwwAAADAzrNmiNTd715vGQAAAICdY8OFtavqlVV123W236aqXrmcYQEAAACwnWw4RErykCRHr7P9RkkevE+jAQAAAGBbWiREmnKVJBctsT8AAAAAton1Cmunqo5KcsO5VTetqjus0vQaSX4vyWeWNzQAAAAAtot1Q6QkD03ytCQ93v54vK1USb43tgcAAADgADMVIr05yRcyhESvTHJCkvetaNNJzknywe7+0rIHCAAAAMDWWzdE6u6PJPlIklTVDZL8dXf/22UxMAAAAAC2j6mZSN/X3U/fzIEAAAAAsH1tOESaqaprJzkmyeFZ5epu3f3aJYwLAAAAgG1kwyFSVV0uyUuT/OesEh7NESIBAAAAHGDWC4NW+n+SPCLJXyZ5cIZi209I8qgkn05yWpK7LXuAAAAAAGy9RUKkByd5a3c/KMnJ47p/6e6XJbl1kmuO9wAAAAAcYBYJkW6cPeHR98b7KyRJd5+b5FUZTnXbkKr6tap6b1V9q6ouqKpPVtWTq+qKc22qqp5UVV+qqvOr6tSqutUqfd28qt5eVedV1Veq6hlVddCKNkvrCwAAAGCnWaSw9vlJLhr/PidJJ7nW3PavJbn+Av0dkeSdSf48ydlJbpPkuCTXSfLosc0TkjwlyeOTnJHkcUlOqapbdvfXkqSqDk9ySpLTkxyb5Ogkz88QkD157vGW2Rc7zDsf+htbPYQD1p1fdeJWDwEAAIANWCRE+mKGUCXdfVFVfSbJPZK8btz+i0m+vtHOuvvlK1a9s6oOS/Koqvr9JFfKEPw8u7uPT5Kqel+SL2QImWahziOTHJzkft29O8nbxn6Oq6o/6+7dVXXlZfW10ecHAAAAcCBZ5HS2dyT51bnl1yV5YFW9s6releT+Sd6wj+P5VpLZ6Wy3T3LYfJ/jaXMnJbnn3D73zFCraT7gOTFDGHTHTegLAAAAYMdZJER6XpL/WlVXGpefneT4JD+Z5BZJTkjytEUHUFUHVdUhVfXzSR6T5H92dye5aZJLMlz5bd4nxm0zN81wetr3dfeZSc6ba7fMvgAAAAB2nA2fztbdX03y1bnlSzKEPo/ZxzGcm+HUtSR5bYaaRUlyeJJzxseZtyvJIVV1xe6+cGx39ir97hq3LbuvS6mqhyd5eJIcddRRazUDAAAA2G8tMhNps9w+yS8k+aMMxayPn9vWq7SvVbat1W4jbfamrx/Q3Sd09zHdfcyRRx65VjMAAACA/daaM5Gqaq+m1Iynfy3S/kPjn++pqrOSvKaqnp9h9s+hVXXQihlEV09yXnfPrhS3a1y30tWyZ1bRMvsCAAAA2HHWO53tC1ln9s06Dtq7oSRJZoHSjTLUJjooyU2SfHKuzcq6RWdkRb2iqrp+kqvMtVtmXwAAAAA7znoh0jOydyHSvvi58f7zSb6cZHeGq749K0mq6pAk985QxHvm5CSPr6pDu/s747oHJDk/ybvH5fcusS8AAACAHWfNEKm7j9vMB66qtyQ5JcnHM1w57ecy1EX6q+7+7NjmOUmeUlW7MswEelyGOk4vmevqZRmKe7+xqp6b5MZJjkvygu7ePT6XC5bVFwAAAMBOtOGrs22CDyZ5SJIbJrk4yeeSPDFDkDPznAxBzxOTHJHktCR36+6vzxp0966qumuGgtwnZahd9MIM4U82qS8AAACAHWXDIdJGC21vtLB2dz8lyVMm2nSSPxlv67U7PcldLqu+gO3tsy9/5lYP4YB09CPW/coGAAAOcIvMRPpCNlYjaV8KawMAAACwDS0SIq1WaPvySY5OcmySj2UoTA0AAADAAWbDIdJ6hbar6sZJ3pehzhAAAAAAB5jLLaOT7v5ckpcnefoy+gMAAABge1lKiDT6cpKbL7E/AAAAALaJZYZI902ya4n9AQAAALBNbLgmUlU9dY1N10hylyS3TPJnyxgUAAAAANvLIldnO26dbV9L8uQkz92n0QAAAACwLS0SIt1olXWd5Nvdfc6SxgMAAADANrThEKm7v7iZAwEAAABg+1pmYW0AAAAADlCLnM6Wqrp9kkcl+ZEkRySpFU26u49e0tgAAAAA2CYWuTrbf0nysiQXJvlkkjM3a1AAAAAAbC+LzER6UpIPJ7l7d5+1SeMBAAAAYBtapCbStZO8QoAEAAAAsPMsEiJ9IsnhmzUQAAAAALavRUKkP0nyX6vqhzZrMAAAAABsTxuuidTdb6yqQ5KcXlVvTvKFJJdculk/c4njAwAAAGAbWOTqbD+a5BlJDk3yO2s06yRCJAAAAIADzCJXZ/uLJNdK8gdJ/jHJrk0ZEQAAAADbziIh0u2SPK+7X7JZgwEAAABge1qksPbuJN/crIEAAAAAsH0tEiK9Icn9NmsgAAAAAGxfi5zO9vIkrxmvzPY/knw+l746W7r7zCWNDQAAAIBtYpEQ6eMZrr52TJJ7r9PuoH0aEQAAAADbziIh0jMyhEgAAAAA7DAbDpG6+7hNHAcAAAAA29gihbUBAAAA2KE2PBOpqu6wkXbdfereDwcAAACA7WiRmkjvysZqIimsDQAAAHCAWSREeuga+x+d5CFJvpDk5fs+JAAAAAC2m0UKa79mrW1V9edJPrSUEQEAAACw7SylsHZ370ryv5L8t2X0BwAAAMD2ssyrs+1KcuMl9gcAAADANrGUEKmqrpzkd5J8bRn9AQAAALC9bLgmUlW9co1N10jys0mOTPL4ZQwKAAAAgO1lkauzPWSN9d9O8qkkj+3u1+/ziAAAAADYdha5Otsy6ycBAAAAsB8RDAEAAAAwad0QqaoOqqrnVNUjJ9r9XlX9aVXVcocHAAAAwHYwNRPptzMUy/7gRLt/TvLfkzxwGYMCAAAAYHuZCpF+Pckp3f0v6zUat781QiQAAACAA9JUiHTrJKdssK93Jjlm34YDAAAAwHY0FSJdI8k3NtjXN8f2AAAAABxgpkKk7yS55gb7OiLJOfs2HAAAAAC2o6kQ6eNJfmmDfd1tbA8AAADAAWYqRHpjkl+sqmPXa1RV98kQIv31sgYGAAAAwPYxFSK9PMlnkryhqv6kqm44v7GqblhVz0ryhiSfGtsDAAAAcIC5/Hobu/v8qvrlJH+X5IlJnlBV30myO8mhSQ5LUkk+meRXuvuCTR4vAAAAAFtgaiZSuvszSW6V5A+SvCfJxUmuk+SSJP84rv/p7v7sJo4TAAAAgC207kykmXGG0UvGGwAAAAA7zORMJAAAAAAQIgEAAAAwSYgEAAAAwCQhEgAAAACThEgAAAAATBIiAQAAADBJiAQAAADAJCESAAAAAJOESAAAAABMEiIBAAAAMEmIBAAAAMAkIRIAAAAAk4RIAAAAAEwSIgEAAAAwSYgEAAAAwCQhEgAAAACTtixEqqr7V9XfVtWXq+qcqvqXqnrgKu3+S1V9uqouGNvcdZU2P1RVbxr7Oauqjq+qQzazLwAAAICdZCtnIj0uyTlJHpvkPknemeT1VfX7swZV9RtJXpbktUnumeTjSf6uqm451+bySd6a5AZJHpDkD5LcP8kJ8w+2zL4AAAAAdprLb+Fj37u7z5pbfkdVXS9DuPSScd3Tk7ymu5+ZJFX17iQ/leQJSX57bHP/JDdLcpPu/vzY7qIkJ1bV07v705vQFwAAAMCOsmUzkVYESDP/muRaSVJVN07yo0neMLfP95L8nwwziWbumeSDs9Bn9OYkFya5x7L7AgAAANiJtlth7dsnOX38+6bj/Rkr2nwiyTWq6si5dj/QprsvTPLZuT6W2RcAAADAjrNtQqSxyPWxSV46rjp8vD97RdNdK7YfvkqbWbvDV7RdRl+rjf3hVXVaVZ32zW9+c61mAAAAAPutbREiVdUNk7w+yd9096tXbO6VzVdZv7LNrN3K9cvsa88O3Sd09zHdfcyRRx65VjMAAACA/daWh0hVdY0kJyc5M3sKXCd7ZgldfcUus+Wz59qtbDNrN99mWX0BAADw/7d353GWVPXdxz9fQESEQQRBxAVQ0aDJk0QhgfggqBFZFFHAHXnUEKMk7iiKOrgkgHFJRCMogksiEVQCAiIgI4KCoJAoCEqEBJAdlE0B4Tx/nLp0Tc3trjtMd9/u6c/79erXzK06t+rcOrWc+tU5pyQtOGMNIiVZE/gmsDqwcynljtbswdhE3bGIngzcXEq5oZVuqTRJVgc2ay1jOpclSZIkSZK04IwtiJRkNerb0Z4I7FhKub49v5TyS+DnwB6t76zSfD65lfRkYMskj2tNewHwYOBb070sSZIkSZKkhWi1Ma7708BOwJuob0j789a8C0opdwGLgS8nuQI4G3g1Nej08lbaY4H3AF9P8l5gHeDjwL+VUn7RSjedy5IkSZIkSVpQxhlEem7z7z8NmbcpcEUp5StJ1gLeCbwXuAjYpZTy00HCUso9SZ4HHAp8FbgLOBp4R3uB07ksSZIkSZKkhWZsQaRSyiYjpvss8NmeNFcBL5zNZUmSJEmSJC0kY387myRJkiRJkuY+g0iSJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdBJEmSJEmSJPUyiCRJkiRJkqReBpEkSZIkSZLUyyCSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSp12rjzoAkaWH7zfmnjDsLK6V1nr7DuLMgSZKklYwtkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSL4NIkiRJkiRJ6mUQSZIkSZIkSb0MIkmSJEmSJKmXQSRJkiRJkiT1MogkSZIkSZKkXgaRJEmSJEmS1MsgkiRJkiRJknoZRJIkSZIkSVIvg0iSJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdBJEmSJEmSJPUyiCRJkiRJkqReBpEkSZIkSZLUyyCSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZIkSZIk9TKIJEmSJEmSpF4GkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSL4NIkiRJkiRJ6mUQSZIkSZIkSb0MIkmSJEmSJKmXQSRJkiRJkiT1MogkSZIkSZKkXgaRJEmSJEmS1MsgkiRJkiRJknqtNu4MSJKk+eN3N1497iyslNZYf+NxZ0GSJKmXLZEkSZIkSZLUyyCSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZIkSZIk9TKIJEmSJEmSpF4GkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSL4NIkiRJkiRJ6mUQSZIkSZIkSb0MIkmSJEmSJKmXQSRJkiRJkiT1MogkSZIkSZKkXgaRJEmSJEmS1MsgkiRJkiRJknoZRJIkSZIkSVKvsQaRkjwhyWFJ/jPJvUmWDEmTJO9OcmWS3yY5M8kfD0m3RZLTk9yZ5FdJPpBk1ZlaliRJkiRJ0kIy7pZITwF2An7e/A3zLuC9wMHA84HbgdOSPHKQIMm6wGlAAXYFPgC8DThwBpclSZIkSZK0YIw7iHRCKeUxpZQ9gIu6M5OsQQ38/EMp5dBSymnAHtQAz76tpK8HHgK8qJRyainlM9Sgz1uTLJruZUmSJEmSJC00Yw0ilVLu60myDbAI+GrrO3cAJwA7ttLtCJxSSrm1Ne1oajDomTOwLEmSJEmSpAVl3C2R+jwZuBf4RWf6z5p57XSXtBOUUv4XuLOVbjqXJUmSJEmStKCsNu4M9FgXuL2Ucm9n+i3AmklWL6Xc3aT79ZDv39LMm+5lLSXJPsA+AI997GP7f5UkSdIsuO6W28adhZXShuuuPe4sSJI0FnO9JRLUMYu6MmTeZOlGSfNAljWRuJTDSylPL6U8/RGPeMSwJJIkSZIkSfPaXA8i3QKsnWTVzvSHAXeWUu5ppXvYkO+vw0SroulcliRJkiRJ0oIy14NIlwCrAk/oTO+OW3QJnfGKkjwGeGgr3XQuS5IkSZIkaUGZ60Gk7wO3AnsMJiRZE3g+cHIr3cnADknaHdRfAvwW+O4MLEuSJEmSJGlBGevA2k0QZ6fm48bAoiS7N59PKqXcmeQg4L1JbqG2BHorNfj1ydaiPgP8HfD1JAcDmwGLgY+VUm4FKKX8brqWJUmSJEmStNCM++1sGwDHdKYNPm8KXAEcRA307A+sB5wP/GUp5brBF0optyR5NnAocAJ17KKPU4M/bdO5LEmSJEmSpAVjrEGkUsoVTLwdbbI0Bfhw8zdVuouBZ83WsiRJkiRJkhaSuT4mkiRJkiRJkuYAg0iSJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdBJEmSJEmSJPUyiCRJkiRJkqReBpEkSZIkSZLUyyCSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSp12rjzoAkSZK00J156dXjzsJKa9snbTzuLEjSSsOWSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZIkSZIk9XJgbUmSJElaDv/wzfPHnYWV0v67PH3cWZDUwyCSJEmSJGml9YKDvjHuLKyUjn/XbuPOgsbA7mySJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdjIkmSJEmSpDnhj1/zqXFnYaV04effOC3LsSWSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZIkSZIk9TKIJEmSJEmSpF4GkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSL4NIkiRJkiRJ6mUQSZIkSZIkSb0MIkmSJEmSJKmXQSRJkiRJkiT1MogkSZIkSZKkXgaRJEmSJEmS1MsgkiRJkiRJknoZRJIkSZIkSVIvg0iSJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdBJEmSJEmSJPUyiCRJkiRJkqReBpEkSZIkSZLUyyCSJEmSJEmSehlEkiRJkiRJUi+DSJIkSZIkSeplEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZIkSZIk9TKIJEmSJEmSpF4GkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSL4NIkiRJkiRJ6mUQSZIkSZIkSb0MIkmSJEmSJKmXQSRJkiRJkiT1MogkSZIkSZKkXgaRJEmSJEmS1MsgkiRJkiRJknoZRJIkSZIkSVIvg0iSJEmSJEnqZRBJkiRJkiRJvQwiSZIkSZIkqZdBpCGSbJHk9CR3JvlVkg8kWXXc+ZIkSZIkSRqX1cadgbkmybrAacDFwK7A44GPUgNuB4wxa5IkSZIkSWNjEGlZrwceAryolHIrcGqSRcDiJIc00yRJkiRJkhYUu7Mta0fglE6w6GhqYOmZ48mSJEmSJEnSeBlEWtaTgUvaE0op/wvc2cyTJEmSJElacFJKGXce5pQk9wDvKKV8ojP9KuCLpZR3D/nOPsA+zccnAZfOeEZn3/rAjePOhEZmec0fltX8YnnNL5bX/GJ5zS+W1/xhWc0vltf8srKW142llOcNm+GYSMMNi6xlkumUUg4HDp/RHI1ZkvNLKU8fdz40Gstr/rCs5hfLa36xvOYXy2t+sbzmD8tqfrG85peFWF52Z1vWLcDDhkxfB/j1LOdFkiRJkiRpTjCItKxL6Ix9lOQxwEPpjJUkSZIkSZK0UBhEWtbJwA5J1m5NewnwW+C748nSnLBSd9dbCVle84dlNb9YXvOL5TW/WF7zi+U1f1hW84vlNb8suPJyYO2OJOsCFwM/BQ4GNgM+BnyilHLAOPMmSZIkSZI0LgaRhkiyBXAosDV1HKTPAYtLKfeONWOSJEmSJEljYhBJkiRJkiRJvRwTaYYkWZykJDllyLxjkyyZ5fz8SZLfJ/mrIfO2SXJfkldOw3oOSnLVA/zuw5L8fZJLkvwuya1Jzkjy4iQZtvwkWzTbeq0VzfsU+Vqc5MaZWv6IefhCsz+9dpz5GEhyVJLzx52P2ZBk7yQ/SnJbkluSXJDkYzO0rj2T7D1k+j5JXjhk+hVJ/nEm8jLdZnM7TrH+MuTvstnKwyiSfCjJtePOx2xoXSdLcw26Jcl5ST6c5JEPYHn7JdluBvJ4Y+vz5s20YW9xnbem4zqXZKMkJyX5TVOm201T9kZd/9CySbJVksWzmZdxmYn6SpIlSY6dzmVqWakub46dJ3TmDd2HZ7J+ujIeN61rzi8mmX9ZM39x83nB1HUHusf7XLgH6ppj9cn7mmvefyX5RJLHD0lfkuw7W/mbLQaRZt5zk2w57kyUUi6gdtE7KMn6g+lJVgU+DSwppXx5XPlL8ijgh8BewGHA86gDmv8Y+ALw3Cbpp4Dnt766BfB+YMaCSOOWZA1gEEB42TjzstAk2Z/anfUU4EXU/fM/gBfM0Cr3BPYeMn0fJvaBeWcM23Eqz6J2VR787T6GPEzlM8BO487ELPoNtRy2AV4KfB14FfCTJE9bzmXtB2w3rbmr++0Orc+bU685K1UQaZq8B/g/1OvU1tTr92yarGy2aqZLc9nWwCbN/1/amTeOfXhlPW5+B2ya5Ontic292uOa+QMfZHidbCHpXgPHag7WJ7cBXgwcQb1X/a8kO3bSbQ0cM8t5m3GrjTsDK7mbgauoFau5cAP4XmAP4CDgdc20fYE/AP5oRRacZHXg9yuwiM8CawBPK6Vc15p+cpJPNfMopVwJXLkC65mPdgYWAacD2yd5ZCllQbRUmAP2BQ4rpby7Ne2EJAeOK0Pz1FzajueVUm4fJWGSh5RSfjvTGWorpVxFvW4sFL8vpZzT+nxKkn8BzgT+PcmTpns8wuUp1wVYHiviycC5pZSTxp0RaR56GXAH9cU+LwM+NN7sIJ0JzAAAHhxJREFUrLTuoAa4Xwq0Wxm9FPgOcP/Di1LKf89u1uaeOXgNnKv1ydOSfAb4JvBvSTYppfwGoFPHWWnYEmlmFeDvgRck+cOpEiZ5bJKjk9yc5M4kpyR5Umv+mUkOa33eoWke99HWtBcnuTvJmkMzU8ptwFuA1yTZuuku8AHgkFLKpa3lrJXk00muT/LbJOcm2b6T33OSfDnJvkkuB34LrDfkd62S5PAkNyb500l+++bUJ+8f7ASQBvn+ZSnl4ibt/d3ZkjyPicjuNc32uCTJhknuSfKSznpWTXJ1kr8flo8VkWTTJMeldsG7LckJQ5ojvzbJRc02vTHJd5M8ZYTFvwy4mnriXIXaWqW93E2a375nksOaZpVXJTkwySqdtHsk+UWThzNSuzmWdLpQJXldk9e7kvxPkv1G2AZT7sNNmv1Tmwv/Lsl1Sb6VB9BtZRY9DFgmYFc6g8klWSPJIUmubLbZfybZqZNmryRnNdvnlmb7P701/yjq04xnZqKZ7OLUrq9PA17dmr73ZBlO8oxm37ozyU1JPptk7RXZCNNg1O14UJKfJLm92Yf/tbt/pOnCl+QtTZpbmv1uhVuGNMs7OMn7k1xNfRBAkr9ojulrmrxdkOSlne++rimbpyQ5LckdSX6WZNch63lxaretwbngxCSPaeYt1Z0tyepJPtbat36V5OtJVmul2bTZBjc15f6faZ3/kmyQ5EutY/M7meR8PBeUUn5NbVX0eOAvof8YS3IF9Rr0/tZxsl0zryR5a2pT8xuAn7S+t29zTryrOTe9pZ2XtJryN8s7oZk16HZyxcxshbkjyUOTHJrk0mb/uTzJp5IsaqUpwLOB3drbJbWucXyz396R5MIkr2h97+Gp14NXd9aZZj0fa017anOs3Nb8HTM4P0xWNs258pODPDZ/S0ZZ5nw3Srk16VZNvTb/vDkOrkq9Hk223HWSnN0cg49opk1Zv0myfmq3/ME5akmWbQkyY+f2uS61V8AewPHA54EtkvxRM29vptiHO8sZtcxLkjelDiFxQ2p9/1NJHty3ziRPbsrlymYdFyV5czr1zTnuaGDP5P6hMkKtWx/dTpROd7ZMdGP6wySnNue0S5K8qPO9JalDl7w89bpya5KTkzy6k26F647tfCZ5YSaGBDkr9UVR7XRrJvnnJNc2ac5L8lymkGW7dD+oOU7/NxN1km+kNiaYDXO2PllKuQv42yaP9/ccyZDubEl2bcrsd015HJLkQZ00vfdsqefvxa3yuCjJyx9I/pfXfDrg56tjgJ9TWyMNleThwFnAk4DXU09kD6VGNR/SJDsT2Lb1tW2pTS67035cSrlzsnWVUr4KfBv4F+DjwA3AhzvJvgC8AlhMvam9nvp0eKtOumdTmxG+DdgVWGq9zUXxKGoTw+1KKZM1bX9m8++3Jsv3JH4ADCLRO1ObC76kCUR9E/h/nfTPBR7V5GnaNBfd06ktuv6K2vR1U+C7TdmSZFtqN5UvAzsCrwG+D6zTs+y1qb/tq6WUS6hPTybr0nYIcDu1e86XgffR6qrTXHSObpaxG7Wy8u9D1vkO6v5xHLBL8/8Pdk+Ane/07sNJ9qKW18eoTWP/BrisSTdX/Rj42ySvTrJMkLTlWGq5/z21u+V5wPFJ/riVZhPgi9SK4supT3bOTLJZM/+DwBnABUx0tfoc8AbgEuCk1vQTh2UiyV9Q98VrqWX/ZmqA9sjl+M0zYdTtuAF1G+5MzftmwHeac0nbntTzzz7AO6n76ajB4VWTrNb6S2f+XsBfUPfjwYV4E+B7wGup57PjgC8l2WPI8r/SzN8NuJzammajwczm4n8scCl1X3gN9ThYf5klVQdQu/YeQA2ovAW4jeb63VSKfgD8KfBW6v53JPCY1jKOp26vt1Cftq4OLGnte3PRGdTWrX/efO47xnajdo07gonjpH3NeQewEbWr3N8BpI4R+Enq9nk+9Xr90STvmiRPPwbe3vz/Rc06dluB3zhfrAmsSq3H7Eht1fwslm6evzX13HUGS2+XxwFnU1s/Px/4GnBkkpcBlFJuBr7Bstfr7ajH3ZEAqQ9lzqa2Sn4VdV94CvUJdJi8bE4EBg/bBvvFG0Zc5nw3SrlBHULgQOCr1HPp25jkutxc60+jnkO2L6XcMGL95jjqdf/t1PPZKsAZ6TxsY8XO7fPZs4ANqXW0Y4F7mKjrTboPDzFqmUMt50cBrwQ+Avw18KYR1rkx9fr1Bmr94rPU/eedI/7WueDr1O39jObz/wUeQT0XjeLfqNeN3YBfAEd3A0TAn1Ef/r6Nuj//KXB4J8101B0HHketX3+wSbcO9d5tjVaaz1LPtR9u8n4lcGKSZzC6/an3iO+l1kneTL32dutpM2Uu1SeX0dyrXcVE3WUZSfak7oM/pNYpD2zW/w+tNCPds1Ebg7yHum+9gHpN+9fBNXZGlVL8m4E/agDmxub/ewP3Aps3n4+ljkE0SPtB4Cbg4a1p61IPyjc2n3egtmx6RPP5TOoYR78H1mqm/Rj4yAh5ezy15VABdujM++Nm+kta01alniT/ozXtHGrAYr3O9w+iHjwPolZIrgKeNMK2uhfq2wJ70h4EXNX6vHuT30d20u3SLHPj1rSvAmetSFlOMv/1TTls1pr2aOBuYP/m89uBHz2Ade/V/L6tms/vaD5v2kqzSTPti53vXggc3fp8DLWZdFrT9mu+u3fzeVFTru/vLOsD1MDEqs3no4Dzl3MfPhT42mwcf9P1R+3m+ctmG90HXNRsi0WtNM9u5j+z890zgWMmWe4q1O7ElwDva01f6tzQmn4+cNSQ6VcA/9j6/D3gjE6aZzX5e+pc3o5DvrMqtbJagG07v/m/gdVa0z4BXNuTh72bZXX/XtdKM2i2vfoUy0lTdkcA325Nf12zvL1a0zZofu/rWr/pWmpQeLLlf6j9W6jB9YOnSP8RalBpg0nm79Lk6y9a09aitrL61Lj2iSYfi5n63HoNNYg90jEG3AgsHrKcAlzQmbYKtYXnkZ3pn6aet9YYlsfW9txknNtutsuik3Y1aqC1AI9tTV8CHDvF9wbHzmHAd1rTn9McJ+1r6BdZ+hrzJeqN6+qtaU+kXud3nqpsqDdyZUh+epc53/6mKsdh5UbtgliAv5timUuo16ZHAP9JvUlpXwOnrN9Qx7hc6vilBqluoHZLGUy7ggdwbl8Z/qitj24Z7IvUIM7lcP9btCfbh6c8bqc4VgtwZiftccA5rc9D19n5zuCYfjfwy3FvxxG28/3bizqOzqea/38aOK75//3XEZat6+7dbLvXtKatR70HeH1r2hLqdWTd1rQ3N999SPN5OuuORzXL2qY17XHtfFEfdN8HvLqzvJ8Cp3TyfmwZss2az98EPjrGMpxL9cm1Jpn/A+Dk1ucC7Nv8P8D/sGzd4zU0vXqaz6Pcsz2c2j3z/Z1lnQRcOtNlYUuk2fFl4H+p0dthngOcCtw6eDpOvSn4ETBosvh9asXmGU3Ll62orRRuBLZObar6R9SbyCmV2sf3G8BPSindt8dt1azn663091IrEN1I9TmllJuGrGK1Jv1W1IP10iFpZtrJ1Ju1vQCSrEuN0B45A+vaitoC7JeDCaX2IT6biW12IfAnST6eZNvlaPb5MuqF+YfN56OpJ5DuoItQW5i1XUwNZg1sCZxQmjNM4/jOd7amVu6OabfWoPYT37CzvLZR9uELgZ1Su9ltNeRpwJxTSvkv6oX3BdRKRqhPX87PxBsBn0Pd187ubLPTmfjtJPmDpsnvddRj7B5qy63NpyOvqd1Ytwa+2snHWc26lneQ4mkz4nYkyY5Jvp/kN9TKz6AffncbnVFKaY/BdjGwwYjH1bbUY2Hwd1xn/mmllLvbE1K73Bya5H+o2/Ie6gV/WNndfxyWUq6nnqMHx80W1ONoec5DFwKvTfL2DO8W/SzgpGZdw2wFXFNKObuVr9upNynL8/RxHAatQUY6xnp0W+89mvoUvvuE/t+pwfQpu6AvNEleldqN83bq/n9WM2vK81eSdVO7T7SPnX063zudWql+dfOdtamtidrHyXOo9Zb7WuV/OfUmYNR9oGsmljmnjFBug6EKjupZ1IbAd6kPi55bSrm1Na+vfrMVcEMp5buDCaWUO6g3o91z0Iqc2+elpk6/G/CN1rXnK9QHhJO2ZphieaMeq311xsmWv0ZTj7sMuKtZx4eBTdPqZj0PHA3s3mz/3el0ZevRvs7fRO2x0d1255VSbml9vrj5d+Pm3+muO15fSvl+K1//Q62DD3qRbEm9ph7TSnNf83l56gIXAnunvg31j2a71eYcq09OZqptsjnwWJatq3+H2ir2qU26Ue7ZnkptfTisHrN5kg0e6A8YhUGkWdDsnIcAr0zyuCFJ1qc2772n87c9TZeEUsczupDa5HIrarTyv6gXh/9LfdKwCjVwMYq7m7+ujYBbSin3dKZfR21Z0p02zCJqE8dT2oGVKVxNzfvGfQlH1QS+vsDEWxVeTj2JfHW61tGyEcO3xXXUKDGllNOoTUi3pUb5b0wdd2rSrlypb9F7DrVp/cNS++jeRm3uOqy/6687n++mGZC88Ujqk7+27udBl5qLWHpfPKOZ/hiG692HqU/a3k1tOnoucF2SD871YFIp5a5SygmllH1LKVtQW5w8kdq1CepvfyTL/vbFNL+9uSn6dvP5rdRjdkvqU912Ga2IdalPWz7dycdd1JaBk5XdrOjbjqlvRjmeeqF/FTUgNqhAd7fRsH091C4WfS4opZzf+uu+unbYsfwlatfeQ6jnti2p55dhZTfVcThoen3NCPkcOJDaVeRvqW/9uDJLdy1dr2d5veenuahpgr8eNZ+9x9gIuttgo0mmDz7P2W0z25LsRm0Z9ANql4o/Z6K7Wt/56yjqteEj1C7lW1KvBfd/r6kkH0kd920wNslq1C4jA+tTuxp094HNeODntplY5pwxYrmtB9zRCQoNswX1xu1LTQDofiPUb5bnHLQi5/b5akfqGContep6S6jX7uXqkrKcx2pfnXEyB1Nbnx1O7c62JRODgE9XfWY2HE9tlfth6sPTE6ZOvpRRtt2wNLTSTXfdcdiDpOuZuNZtBNxelh3y5DpgzSaYNooPUd+U/YYmH1cmedPUX5lec6g+OZmNmfweeXCfdRJLl/vlzfTBtWeUe7a+ekz3vn1azaeI8Xz3eeqYFsP6DN9M3dk/OGTeba3/f496ArkJOLuUcl+S71Hf/PYg4OJJWgYtj2uAdZM8qBNI2pDa1LatMNzN1LGBjktybSnl/T3rHDyd2oHaRWS6HAG8K8k21GDSsU0wbrpdQx1HoWtDmoF5AUopXwC+kDoQ5YuoY1LdCkw2/sYe1GP0TUz0U79fkqeWUn66HPm8ltocva37eZDfXRh+ApysVVnvPtw88fg48PHUQYRfQb14X029SZ4XSilHJDmE2g0A6m+/mqnfwLg19SnVX5baXxqoA5ROY9Z+TT0mF1MvTl2/msZ1rbAh23E36gXyJYMnL5ME3Wc8a+0PzY3QjsA+pZTPtaY/kODn4Py8EfWhQH9m6lvEDgAOSH0JwRuATya5pLl5u4mJisQw11C71XUtdX6ag7annv9+QG1t1XeM9elerwaBt+622bD5dy5vm9m2B/Wta/ePw5LkmX1fagKBO1Ob8X+mNX3YA8wjqa8T3556vT6u8xR/MHbS55b9Kt1A8KhmYplzySjldhPw0CSLegJJZ1DHvDo8yY2llKVuuHvqN/P1HDRbBoGiYeMW7ZnOYP89HtCxupz2AD5ZSjmktY6dp3kdM66UckeSb1LHCjymGxydBdNddxx2jG1AfSgM9ThcK8manUDShsCdpQ4K3auU8jvqmKvvS/JE6pAen0hyaSllece2nRZzqT6Z5A+oZfaDSZIMznn7UM+pXYNg0ij3bO16TPv+f1bqMbZEmiXNwfmP1C4Q3Qr/6dQgxEWdJ+Tnd7qCfQ/4E2rk/8xm2pnUwduezQhd2UbwQ2prhvsHC21ull7MRJPYXqWUk6lBgvckeVtP2p9Tb3rf11RAlpL65qEtlv0msGxkv73c/6YGqA6iNg2dia5sUFvVPC3JpoMJSTYGtmHINiul3FBKOYxaXpP9LqgVi59RK9Xtv+dRo9bDurRN5Tzg+Z2mpy/opPkBtZXbo4bsi+dPEYQbdR8GoJRyZSnlIOqAwlNtg7Ea1hS02UfXYSLIdjr1icHtw7ZZk2YwQP5dreVsQ22u3jbZk8DeJ4RNBegc6hhkw8pubEGkEbfjQ4B7Ok13X9H93hisQX0q1S67daiB1uV1MbVi8OoHkpHmXPlWaqvKwXFzOrWb6DLnzsa5wKOa/Q24PzC2E8txTp9NzZP4g6nnh9MY7RiD0Z+kQ31C+SvqDVHbntSb358s842JdbAc61kZPITW/t8Y5dh8MLU+0T521mbZ6w6llCupT9wPpHat6F6vT6c23f/RkH3giibNZGVzd7Pu7vRRljmfjVJu32n+3atvYaWUD1MHWz4mybMmSTOsfnMutXvI/S+CSe1+vTNz9Bw0W5ruN7tQu69163pvpd4Mbs/k+3DXAz1Wh5lsnUuto7lHWN766FzxL9QWSON4kDmddUeox1j7Ov9Y6mDeg+EwzqM+TGm/cCfN5wd0HJZSfkFtlXYXs1SXn8v1yaY11z9TH+pO1j3yUmrwcJNJ6uqDYNAo92w/pb7Ualg95uellG7LpWllS6TZdRi1O882TLS+gTqa/iupo8Z/krpzbUh9a9lZpZSvNOm+R62QbUMd7R9qU8J7qM0bP7GiGSylXJjk69SnTQ+njlPwN9QT1nIdgKWUY5O8hvomlltLKZ+dIvlfUbfJj1Jf6XsB9SSwPfXJ++5M9CduG0Tm35Dka9ST8UWt+UdQu6L8NxOBtwdi9SS7D5n+XWpz/XcCJyd5H7XP8mLqk8zDAJIcSG22vaSZ/ifU8h3aCin1LQ/PoA7MvWTI/G9Rg0wHLMdvOJhamTs6yZFMvE0O6uB0lFJ+nWQx8E9N1P5MarB5c+qbWCZ7E1HvPpzkMGpU/BzqgIPbU5ufzuU3evwkyX9Qb26upw5U+HbqSfsLTZpTgVOAU5McTH3qs4g6SP0apZT9mRiI/rPN05JHU/eRqzvruwTYNckLaW5ym+DPJcAOSXagPm24fJJWh/sBpye5jzou2W3Uvtc7A+9pghDjMOp2fHOST1ArddtQ96mxKqXclOQCYHGSwZPK/aktM9dczmXdm+Sd1Cf2dzPxpo1nU7uJLPNUKsnx1OP2AuobOfdsZg0eGnyUup3OSvJh6n6zBfDgUspHSyknJjmXeuM3yPd+1NarH2X8VksyaGa+NnXsrr+hbtvnNdtslGMM6nGyc3N+vJ06sOTQwHepLXkXA4cluYm6/z2zWfe7m6etwwyC4n+d5GjqE9zJAk7zzWTXuQup+/97qPviTtR9dkqllN8kOY/6gOhW6nXmXdTz/6IhXzmC2hrjKmp5tC2m3gydmOTz1OvoxtTupUc118nJymZQT3hTku8AtzYPN0ZZ5nw0uHE6FfjUVOVWSrk0yeHUtxJuQL3mPwzYvZSyTGCglPKuJhD4H0n+spRyTl/9ppRySpKzqW+qfBf1GvZ2ah3vI9P70+edXannun8qpZzbntFss/dQ63qD62R3H+7qLfPlMNlxcyrwxtQxkW4G3kgNGM87zTG+ZEyrn866I9Rj70tJ3kt9GPwBan3rKIBSys+SfAU4NHUc3cuo9wBPpl73RpLkG9Sxli5o1rM7NZ6wIvdYy2Mu1Se3TPJb6jH8VOobDjehnj9/M+wLTd3jbdSyWkQdw/duajfqFzbfvZPR7tlubn7jAUl+T30Jz4uox71vZ5uvf0zyxgRqEKnQeQMTdYDPI6lR1LuoAzt+GXhKJ93PqCOxP6g17WQ6b14YIX9H0XrjQGfeWtTo/A3Um5ZzgWd10pwDfHnId5d6e1oz7Q3UwMrLevK0LvX1hpc2672VenLfC1hliuXvTx24/F7gks68RdSD7YAVLMsyyd92TZrNqAP03kY94X8TeGJrGbtQnzoMtuml1ArW0DfSUU+I9wKPnmT+ns36/4yJt7Pt0lfGzfcua/JwFnXMpQK8sJPuldSLxG+pN53nAm/tWfaU+zC1i8LZ1ErHndQxvV477mO1p+zfSL1Q/arZZldQx+l4cifdg6lP0C+jXgyupb5Va+dWmudRnxoMxjPbiWXfgrE+tXvFzU25LG7tX6dRb77ab2a4gtbb2Zppf9as+1bqueJiapBvnXmwHfejvnL2jub3PpHWWy2m+M17M8WbMpYjzVXAQUOmb07tznEHNbD+NpZ9i9rg7Wxr9C2TWun6cXOc3Eit5Dy6mddd7jupx+JvqOeXc1j2WN+UevP96+bYuhDYozV/A+qxeEuz/50B/OkcOL4WM3Euva/J//nUbq7dN26Ocow9rdk+d7D0+Xmpfaiz3H1by/wl8JYhebyxM+1tzX7we+CKcW/HGSiL7t+zqS2pr6eeV75GPc8sdd1hyNvZgCdQW7vcQb1O7zdsmzZp16A+FPvQJHl8MjU4fnOzH19GfVDz6FaaZcqG2pLwEOr55z6Wfjtu7zLn0x/1xuPq5v+rjlhuq9K8Xas5Dq6i9eagbrk22/Mo6vnk/zBC/YbaDeOLTJyDvgts2cn7FTyAc/t8/qPWFX8+xfxPN9vswcP24e6xtBxlvsw5cciyhh431AeE32iWf12T5q/mQzl1f+MkaUZ5O9tane8ste92j5lm2nbNd5/amjZddcejmAgg/Jxatzibzlt5qcGOTzJRTz+fZd/S3V12d794R/O9QZ3kXGDXWSzDuVSfHPzdRm29/E/A44ekH3a87Uh9GHhHcyxdSK3/td8U13vPRj3mD2x+693UOv8rZqMsBq+OlFZKSV5EvbnapNTm8mpJ8kpqS63NSimXjzs/kqSFKclO1JvqzUspl407P/NRkmOBjUspW487L5JmR5KjqAGjleKtkhpurt2z2Z1NK6VmTKLNqVHdbxhAqpL8C7WZ5y3UvtIHACfOhZORJGnhSfIo6lPig4CTDCAtvyRPoXYR34U6QLkkaR6b6/dsBpG0svpbapewHwJvHnNe5pL1qM2j16OOS/Dv1CafkiSNwz7UyvGPqdduLb9DgcdTu1N8bMx5kSStuDl9z2Z3NkmSJEmSJPVaZdwZkCRJkiRJ0txnEEmSJEmSJEm9DCJJkiRJkiSpl0EkSZKkOSzJkiRXjDsfkiRJBpEkSZJmWZI1k7w5yfeS3JzkniTXJTkpyd5JpnyDbpPGt49KkqRZ5dvZJEmSZlGSJwAnApsDpwHfBm4ENgCe0/x9pJSyX5N+dWqd7a7WMpYAm5RSNpnVzEuSpAVtyqdckiRJmj5JHgJ8E9gMeHEp5eudJAcn2RLYcjChlHL3LGZRkiRpUnZnkyRJmj2vA54EfHRIAAmAUsp5pZRPDz53x0Rq/v9M4HFJSutvuyTHJ7kjyaLucpNs1aR773T/KEmStDAYRJIkSZo9uzf/Hr4Cy3gzcAm1C9yrWn8/a5a7JvCyId97DXAfcNQKrFuSJC1gjokkSZI0S5LcBDyolLJMS6EpvrOEzvhHk42JlGRV4HLg2lLKVq3pawLXAGeXUnZagZ8gSZIWMFsiSZIkzZ5FwK0ztfBSyr3A54Etk/xha9buzbqPmKl1S5KklZ9BJEmSpNlzK7D2DK/jCOBe4LWtaa8FrgeOn+F1S5KklZhBJEmSpNnzU2BRks1magWllCuBbwGvTLJ6kicA2wJfLKXcM1PrlSRJKz+DSJIkSbPna82/r1vB5fQNank4sB7wQiZaJNmVTZIkrRCDSJIkSbPnc8ClwNuT7DosQZKnJXlDz3JuB9ZNkknmnwhcDfw18GrqgNqXPMA8S5IkAbDauDMgSZK0UJRS7kyyCzXIc1ySbwOnAjcBjwC2B3YADulZ1DnALsChSb5PHQPpO6WU65v13JvkSOCAJv27p/3HSJKkBSel9LWGliRJ0nRKsia1ldCLgacAawE3A+cDRwP/1rxpjSRLgE1KKZu0vv9Q4J+pgaT1qa3Lty+lLGmleRzwS+AOYKNSyh0z/bskSdLKzSCSJEnSSijJRsCVwBGllL8ed34kSdL855hIkiRJK6e/AValDrItSZK0whwTSZIkaSWS5KXAY4F3AKeUUn405ixJkqSVhN3ZJEmSViJJCvA74HvA/yulXD3mLEmSpJWEQSRJkiRJkiT1ckwkSZIkSZIk9TKIJEmSJEmSpF4GkSRJkiRJktTLIJIkSZIkSZJ6GUSSJEmSJElSr/8PEk08IakNonMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot('City','Profit',data=city.head(10),kind='bar',aspect=2,height=8,palette='RdBu')\n",
    "plt.title('Top 10 cities with profit inflow',size=25)\n",
    "plt.xticks(size=15)\n",
    "plt.yticks(size=15)\n",
    "plt.ylabel('Cumulative profit',size=18)\n",
    "plt.xlabel('City',size=18)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### From above Data Visualization we can conclude as follow:\n",
    "#### Data Quality: Good quality data with no need for data preprocessing. No null values in Data set.\n",
    "#### Sales: 22,97,201\n",
    "#### Profit: 2,86,397\n",
    "#### 'Standard Class' accounts for the majority of profit.\n",
    "#### 'HomeOffice' segment generates least sale.\n",
    "#### In central region Furniture incures loss.\n",
    "#### 'West' and 'East' have noticeably more profit.\n",
    "#### 'Florida', 'Oregon', 'Arizona', 'Illinois', 'Texas', 'Pennsylvania', 'Tennessee', 'North Carlina', 'Colorado' and 'Ohio' have noticeably less Profit."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
