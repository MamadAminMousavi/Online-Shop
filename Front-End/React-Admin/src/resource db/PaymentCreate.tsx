import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const Payment_Creat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="order id" validate={[required()]} />
            <TextInput source="payment method" validate={[required()]} />
            <TextInput source="amount"/>
        </SimpleForm>
    </Create>
);