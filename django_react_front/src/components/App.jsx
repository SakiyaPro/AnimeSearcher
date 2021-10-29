import React from "react";
import "../App.scss";
import { Header } from "./Header";
import { Search } from "./Search";
import { Genre } from "./Genre";

//apiを取得したらreturnのSearchタグの{}はsearch(小文字)に変更

export const App = () => {
    return (
        <>
            <Header
                headertext={"AnimeSearcher"}
            />
            <Search
            />
            <Genre
            />
        </>
    );
};