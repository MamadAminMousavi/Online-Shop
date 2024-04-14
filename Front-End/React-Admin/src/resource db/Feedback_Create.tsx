import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const Feedback_Creat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="user_id" validate={[required()]} />
            <TextInput source="order_id" multiline={true}/>
            <TextInput source="rating"/>
            <TextInput source="comment"/>
        </SimpleForm>
    </Create>
);