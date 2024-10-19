import { useQuery } from "react-query";
import axios from "axios";

export const useFetch = () =>
    {
        const Get_Request = async () =>
        {
            //Need to change url because external IP always changes when launching instance
            const {data} = await axios.get(`http://127.0.0.1:8000`)
            return await data
        }

        const {data, status} = useQuery({queryKey: [], queryFn: () => Get_Request(), refetchInterval: 5000})

        return status !== "success" ? [] : data
    }