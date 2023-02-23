import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from "axios";
import { useNavigate } from 'react-router-dom';


function CreatePost() {
    let navigate = useNavigate();

    const initialValues = {
        title: "",
        description: "",
        graphics: "",
    };

    const validationSchema = Yup.object().shape({
        title: Yup.string().required(),
        description: Yup.string().required(),
        graphics: Yup.string().required(),
    });

    const onSubmit = (data) => {
        axios.post("http://localhost:3001/graphics", data, {
            headers: {
                accessToken: localStorage.getItem('accessToken')
            },
        }).then((response) => {
            navigate("/");
        }
        )
    };

    return (
        <div className='createGraphicPage'>
            <Formik initialValues={initialValues} onSubmit={onSubmit} validationSchema={validationSchema}>
                <Form className='formContainer'>

                    <label> Title: </label>
                    <ErrorMessage name="title" component="span" />
                    <Field
                        autocomplete="off"
                        id="inputCreatePost"
                        name="title"
                        placeholder="Title ..." />

                    <label> Description: </label>
                    <ErrorMessage name="description" component="span" />
                    <Field
                        autocomplete="off"
                        id="inputCreatePost"
                        name="description"
                        placeholder="Description ..." />

                    <label> Link to your graphics: </label>
                    <ErrorMessage name="graphics" component="span" />
                    <Field
                        // autocomplete="off"
                        id="inputCreatePost"
                        name="graphics"
                        placeholder="Link ..." />

                    <button type="submit"> Submit </button>

                </Form>
            </Formik>
        </div>
    );
}

export default CreatePost
