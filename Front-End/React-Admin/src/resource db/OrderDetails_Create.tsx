import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const OrderDetails_Creat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="order id" validate={[required()]} />
            <TextInput source="product id" validate={[required()]} />
            <TextInput source="quantity"/>
            <TextInput source="unit_price"/>
        </SimpleForm>
    </Create>
);