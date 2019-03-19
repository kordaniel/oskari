[User|(pk) id:Integer; role: Integer; username:String; passHash: String; firstname:String; surname:String; email:String],
[Portfolio|(pk) id:Integer;(fk) user_id: User; name:String],
[Trade|(pk) id:Integer; (fk) portfolio_id:Integer;datecreated:date; datemodified:date; amount:Integer; buyprice:Integer; sellprice:Integer],
[TradeStock|(fk) trade_id:Integer; (fk) stock_id:Integer],
[Stock|(pk) id:Integer; date_created:Datetime; date_modified:Datetime; ticker:String; name:String],
[User]1-*[Portfolio],
[Portfolio]1-*[Trade],
[Trade]1-*[TradeStock],
[TradeStock]*-1[Stock]
