import { useQuery } from "react-query";
import axios from "axios";

export const useFetch = () =>
    {
        const Get_Request = async () =>
        {
            const {data} = await axios.get(`http://127.0.0.1:8000`)
            return await data
        }

        const {data, status} = useQuery({queryKey: [], queryFn: () => Get_Request(), refetchInterval: 1})

        return status !== "success" ? [] : data
    }