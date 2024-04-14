import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput } from 'react-admin';

export const Payment_Creat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="id" reference='Orders'/>
            <TextInput source="payment_method" validate={[required()]} />
            <TextInput source="amount"/>
        </SimpleForm>
    </Create>
);