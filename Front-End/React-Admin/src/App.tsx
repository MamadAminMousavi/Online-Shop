import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { dataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import { UsersList } from "./resource db/Users";
import { UsersCreate } from "./resource db/Userscreate";
import { OrdersList } from "./resource db/orders";
import { OrderCreat } from "./resource db/orderCreate";
import { Order_details_list } from "./resource db/orderdetails";
import { OrderDetails_Creat } from "./resource db/OrderDetails_Create";
import { Payment_list } from "./resource db/payments";
import { Payment_Creat } from "./resource db/PaymentCreate";
import { CategoryList } from "./resource db/category";
import { CategoryCreat } from "./resource db/categoryCreat";
import { Product_list } from "./resource db/Products";
import { Products_Creat } from "./resource db/Products_Create";
import { Feedback_List } from "./resource db/Feedback_list";
import { Feedback_Creat } from "./resource db/Feedback_Create";
import { ShippingAddresses_List } from "./resource db/ShippingAddresses_List";
import { ShippingAddresses_Creat } from "./resource db/ShippingAddresses_Create";

export const App = () => (
  <Admin dataProvider={dataProvider} authProvider={authProvider}>
    <Resource
      name="Users"
      list={UsersList}
      edit={EditGuesser}
      show={EditGuesser}
      create={UsersCreate}
    />
    <Resource
      name="Orders"
      list={OrdersList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={OrderCreat}
    />
    <Resource
      name="Order_Details"
      list={Order_details_list}
      edit={EditGuesser}
      show={ShowGuesser}
      create={OrderDetails_Creat}
    />
    <Resource
      name="Payments"
      list={Payment_list}
      edit={EditGuesser}
      show={ShowGuesser}
      create={Payment_Creat}
    />
    <Resource
      name="Categories"
      list={CategoryList}
      edit={EditGuesser}
      show={ShowGuesser}
      create={CategoryCreat}
    />
    <Resource
      name="Products"
      list={Product_list}
      edit={EditGuesser}
      show={ShowGuesser}
      create={Products_Creat}
    />
    <Resource
      name="Admin Logs"
      list={ListGuesser}
      edit={EditGuesser}
      show={ShowGuesser}
    />
    <Resource
      name="Feedback"
      list={Feedback_List}
      edit={EditGuesser}
      show={ShowGuesser}
      create={Feedback_Creat}
    />
    <Resource
      name="ShippingAddresses"
      list={ShippingAddresses_List}
      edit={EditGuesser}
      show={ShowGuesser}
      create={ShippingAddresses_Creat}
    />
  </Admin>
);
