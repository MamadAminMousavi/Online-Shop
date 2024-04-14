import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required ,ReferenceInput } from 'react-admin';

export const OrderDetails_Creat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="order_id" reference='Orders'/>
            {/* <ReferenceInput source="product_id" reference='Products'/> */}
            <TextInput source="quantity"/>
            <TextInput source="unit_price"/>
        </SimpleForm>
    </Create>
);