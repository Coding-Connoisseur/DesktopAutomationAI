const { createLogger, transports, format } = require('winston');

const logger = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp(),
    format.json()
  ),
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'application.log' })
  ]
});

/**
 * Logs an error message.
 * @param {Error} error - The error object.
 */
function logError(error) {
  logger.error({
    message: error.message,
    stack: error.stack
  });

  // Error handling strategies:
  // 1. Implement global exception handlers
  // 2. Use structured logging for consistency
  // 3. Add retry logic for transient errors
  // 4. Implement fallback functions for critical operations
  // 5. Monitor logs for real-time issue detection
}
