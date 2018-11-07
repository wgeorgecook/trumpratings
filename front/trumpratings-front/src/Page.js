import React, { Component } from 'react';
import * as ApiData from './apiData.js';


class Page extends Component {

    tweets = []

    getAll() {
        ApiData.getAll()
        .then( (tweet) => this.tweets.append(tweet) )
      }

  render() {
    return (
      <div className="Page">
        <ul class="tweets">
            { this.tweets.map( (tweet) =>
                <li> { tweet.approval_num } </li>
            )
            }
        </ul>
      </div>
    );
  }
}

export default Page;
