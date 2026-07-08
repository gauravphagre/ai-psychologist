import axios from "axios";

import {
  ChatRequest,
  ChatResponse,
} from "../types/api";


const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
//   baseURL: "http://localhostcalhost:8000"
});

export async function sendMessage(
  request: ChatRequest
): Promise<ChatResponse> {
  const response = await api.post<ChatResponse>(
    "/chat",
    request
  );

  return response.data;
}