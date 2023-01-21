import { createStore } from "vuex";

interface IState {
  token: string;
  isAuthenticated: boolean;
}

export default createStore({
  state: {
    token: "",
    isAuthenticated: false,
  },
  getters: {},
  mutations: {
    // mutations must be called to modify state, state cannot be mutated directly
    initializeStore(state: IState) {
      const token = localStorage.getItem("token");
      if (typeof token === "string") {
        state.token = token;
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
  actions: {},
  modules: {},
});
