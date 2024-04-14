import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput} from 'react-admin';

export const Feedback_Creat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <ReferenceInput source="order_id" reference='Orders'/>
            <TextInput source="rating"/>
            <TextInput source="comment"/>
        </SimpleForm>
    </Create>
);