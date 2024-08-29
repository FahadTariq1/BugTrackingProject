<template>
  <div class="bug-details">
    <div v-if="bugs.length">
      <DataTable :value="bugs" tableStyle="min-width: 50rem" class="p-datatable-header-color">
        <Column field="description" header="Details" />
        <Column field="status" header="Status" />
        <Column field="due_date" header="Due Date" />
        <Column field="assigneduser" header="Assigned To" />
        <Column header="Action">
          <template #body="{ data, index }">
            <div class="action-item">
              <i class="fas fa-ellipsis-v action-icon" @click="toggleDropdown(index)"></i>
              <div v-if="activeDropdown === index && userType !== 'developer'" class="dropdown-menu">
                <ul>
                  <li @click="changeStatus(data, 'pending')">Pending</li>
                  <li @click="changeStatus(data, 'inprogress')">In Progress</li>
                  <li @click="changeStatus(data, 'closed')">Closed</li>
                  <li @click="deleteBug(data)">Delete</li>
                </ul>
              </div>
            </div>
          </template>
        </Column>
      </DataTable>
    </div>
    <div v-else class="no-bugs-message">
      No bugs available for this project.
    </div>
  </div>
</template>

<script>
import {jwtDecode} from 'jwt-decode';
import { updateBugStatus, deleteBug } from '../servicesfile/service'; 
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

export default {
  name: "BugDetails",
  components: {
    DataTable,
    Column
  },
  props: {
    bugs: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      activeDropdown: null,
      userType: ''
    };
  },
  methods: {
    toggleDropdown(index) {
      this.activeDropdown = this.activeDropdown === index ? null : index;
    },
    async changeStatus(bug, status) {
      const success = await updateBugStatus(bug.id, status);
      console.log(bug.status)
      if (success) {
        console.log(`Bug ${bug.id} status changed to ${status}.`);
        this.$emit('update-bugs'); 
      }
      this.activeDropdown = null;
    },
    async deleteBug(bug) {
      const success = await deleteBug(bug.id);
      if (success) {
        console.log(`Bug ${bug.id} marked as deleted.`);
        this.$emit('update-bugs'); 
      }
      this.activeDropdown = null;
    }
  },
  mounted() {
    const token = localStorage.getItem('authToken');
    if (token) {
      try {
        const decoded = jwtDecode(token);
        console.log("decoded")
        this.userType = decoded.user_type;
      } catch (error) {
        console.error('Error decoding token:', error);
      }
    }
    console.log(this.bugs);
  }
}
</script>
<style scoped>

.bug-details {
  font-family: Arial, sans-serif;
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
}

.action-item {
  position: relative; 
}

.action-icon {
  cursor: pointer;
  font-size: 18px;
  color: #333;
}

.dropdown-menu {
  position: absolute;
  top: 20px;
  right: 0;
  background-color: white;
  border: 1px solid #ccc;
   z-index: 1000;
  width: 150px;
}

.dropdown-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.dropdown-menu li {
  padding: 10px;
  cursor: pointer;
  border-bottom: 1px solid #ddd;
}

.dropdown-menu li:last-child {
  border-bottom: none;
}

.dropdown-menu li:nth-child(1) {
  color: red; 
}

.dropdown-menu li:nth-child(2) {
  color: blue;
}

.dropdown-menu li:nth-child(3) {
  color: green; 
}

.dropdown-menu li:nth-child(4) {
  color: red; 
}

.dropdown-menu li:hover {
  background-color: #f5f5f5;
}

.no-bugs-message {
  font-style: italic;
  color: #888;
}
</style>
