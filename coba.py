
#         # # Normalisasi data menggunakan MinMax
#         # data_ternormalisasi_minmax = minmaxscaler.transform([statistik])[0]

#         # # Prediksi label emosi dengan normalisasi MinMax
#         # label_emosi_minmax = knn_minmax.predict(data_ternormalisasi_minmax.reshape(1, -1))[0]

#         st.write("Emosi Terdeteksi (ZScore):", label_emosi_zscore)
#         # st.write("Emosi Terdeteksi (MinMax):", label_emosi_minmax)
#         # Memuat model KNN untuk kategori emosi dengan normalisasi MinMax
# with open('best_knn_model_minmax.pkl', 'rb') as file:
#     knn_minmax = pickle.load(file)
# # Memuat model KNN untuk kategori emosi dengan Grid Search
# # with open('-.pkl', 'rb') as file:
# #     knn_minmax = pickle.load(file)
# # Memuat model dan skalar MinMax yang telah dilatih
# with open('minmax_scaler.pkl', 'rb') as file:
#     minmaxscaler = pickle.load(file)