const DeleteConfirm = () => {
  if (confirm("Are you sure you want to delete your account?") === true) {
    document.getElementById("deleteProfile").submit();
  }
};
