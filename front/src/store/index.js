import { createStore, createLogger } from "vuex";

const debug = process.env.NODE_ENV !== "production";

export default createStore({
  state: {
    user: {
      username: "",
    },
    isAuthenticated: false,
    token: "",
  },
  mutations: {
    // mutations must be called to modify state, state cannot be mutated directly
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  modules: {},
  strict: debug,
  plugins: debug ? [createLogger()] : [],
});
