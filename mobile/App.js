import { useMemo, useRef, useState } from "react";
import {
  KeyboardAvoidingView,
  Platform,
  Pressable,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  View,
  useWindowDimensions,
} from "react-native";

import {
  FEATURE_IDEAS,
  QUICK_AREAS,
  SUGGESTIONS,
  USER_MODES,
  respond,
} from "./src/assistant";

const COLORS = {
  bg: "#F4F7FB",
  card: "#FFFFFF",
  primary: "#135491",
  primaryDark: "#0F3F73",
  primarySoft: "#EAF3FF",
  text: "#0F172A",
  muted: "#64748B",
  border: "#D8E2EF",
  success: "#0F766E",
  successSoft: "#ECFDF5",
  warning: "#B45309",
  warningSoft: "#FFF7ED",
  disabled: "#94A3B8",
};

const INITIAL_MESSAGES = [
  {
    id: "intro",
    role: "assistant",
    area: "Inicio",
    title: "Asistente listo",
    text: "Hola, Areli. Tengo listo el espacio para ordenar código, tareas, SQL, Git, seguridad e ideas de producto. Escribe como te salga; yo convierto la idea en pasos claros.",
  },
];

function createId() {
  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function MessageBubble({ message }) {
  const isUser = message.role === "user";

  return (
    <View style={[styles.messageRow, isUser && styles.messageRowUser]}>
      <View style={[styles.bubble, isUser ? styles.userBubble : styles.assistantBubble]}>
        {!isUser && (
          <View style={styles.messageMeta}>
            <Text style={styles.areaText}>{message.area}</Text>
            <Text style={styles.titleText}>{message.title}</Text>
          </View>
        )}

        <Text style={[styles.messageText, isUser && styles.userMessageText]}>
          {message.text}
        </Text>

        {!isUser && message.insights?.length > 0 && (
          <View style={styles.chipWrap}>
            {message.insights.map((item) => (
              <View key={item} style={styles.insightChip}>
                <Text style={styles.insightChipText}>{item}</Text>
              </View>
            ))}
          </View>
        )}

        {!isUser && message.actions?.length > 0 && (
          <View style={styles.chipWrap}>
            {message.actions.map((action) => (
              <View key={action} style={styles.actionChip}>
                <Text style={styles.actionChipText}>{action}</Text>
              </View>
            ))}
          </View>
        )}
      </View>
    </View>
  );
}

function QuickChip({ label, onPress }) {
  return (
    <Pressable
      style={({ pressed }) => [styles.quickChip, pressed && styles.pressed]}
      onPress={onPress}
    >
      <Text style={styles.quickChipText}>{label}</Text>
    </Pressable>
  );
}

function ModeChip({ mode, active, onPress }) {
  return (
    <Pressable
      style={({ pressed }) => [
        styles.modeChip,
        active && styles.modeChipActive,
        pressed && styles.pressed,
      ]}
      onPress={onPress}
    >
      <Text style={[styles.modeChipText, active && styles.modeChipTextActive]}>
        {mode.label}
      </Text>
    </Pressable>
  );
}

function InfoLine({ number, label }) {
  return (
    <View style={styles.infoLine}>
      <Text style={styles.infoNumber}>{number}</Text>
      <Text style={styles.infoText}>{label}</Text>
    </View>
  );
}

function InsightPanel({ count, selectedMode, onModeChange, onSuggestion }) {
  const currentMode =
    USER_MODES.find((mode) => mode.id === selectedMode) || USER_MODES[0];

  return (
    <View style={styles.insightPanel}>
      <Text style={styles.panelEyebrow}>Workspace</Text>
      <Text style={styles.panelTitle}>VitraMind AI</Text>
      <Text style={styles.panelCopy}>
        Asistente personal para desarrollo, organización y decisiones técnicas.
      </Text>

      <View style={styles.metricRow}>
        <View style={styles.metricBox}>
          <Text style={styles.metricValue}>{count}</Text>
          <Text style={styles.metricLabel}>mensajes</Text>
        </View>

        <View style={styles.metricBoxAlt}>
          <Text style={styles.metricValue}>{USER_MODES.length}</Text>
          <Text style={styles.metricLabel}>modos</Text>
        </View>
      </View>

      <View style={styles.focusBox}>
        <InfoLine number="01" label="Detecta tema, energía y formato." />
        <InfoLine number="02" label="Propone acciones después de responder." />
        <InfoLine number="03" label="Mantiene contexto reciente del chat." />
      </View>

      <Text style={styles.panelSection}>Modo de respuesta</Text>

      <View style={styles.modeWrap}>
        {USER_MODES.map((mode) => (
          <ModeChip
            key={mode.id}
            mode={mode}
            active={mode.id === selectedMode}
            onPress={() => onModeChange(mode.id)}
          />
        ))}
      </View>

      <Text style={styles.modeDescription}>{currentMode.description}</Text>

      <Text style={styles.panelSection}>Prueba esto</Text>

      {SUGGESTIONS.slice(0, 3).map((suggestion) => (
        <Pressable
          key={suggestion}
          style={({ pressed }) => [styles.sideSuggestion, pressed && styles.pressed]}
          onPress={() => onSuggestion(suggestion)}
        >
          <Text style={styles.sideSuggestionText}>{suggestion}</Text>
        </Pressable>
      ))}

      <Text style={styles.panelSection}>Podemos agregar</Text>

      {FEATURE_IDEAS.slice(0, 3).map((idea) => (
        <View key={idea} style={styles.ideaItem}>
          <Text style={styles.ideaText}>{idea}</Text>
        </View>
      ))}
    </View>
  );
}

export default function App() {
  const [messages, setMessages] = useState(INITIAL_MESSAGES);
  const [input, setInput] = useState("");
  const [selectedMode, setSelectedMode] = useState("normal");

  const scrollRef = useRef(null);
  const { width } = useWindowDimensions();
  const isWide = width >= 900;

  const userMessagesCount = useMemo(
    () => messages.filter((message) => message.role === "user").length,
    [messages]
  );

  const selectedModeLabel = useMemo(() => {
    return USER_MODES.find((mode) => mode.id === selectedMode)?.label || "Normal";
  }, [selectedMode]);

  const sendMessage = (value = input) => {
    const text = value.trim();

    if (!text) return;

    const userMessage = {
      id: createId(),
      role: "user",
      text,
    };

    const assistantResponse = respond(
      text,
      [...messages, userMessage],
      selectedMode
    );

    const assistantMessage = {
      id: createId(),
      role: "assistant",
      ...assistantResponse,
    };

    setMessages((current) => [...current, userMessage, assistantMessage]);
    setInput("");

    setTimeout(() => {
      scrollRef.current?.scrollToEnd({ animated: true });
    }, 80);
  };

  const clearChat = () => {
    setMessages(INITIAL_MESSAGES);
    setInput("");
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor={COLORS.bg} />

      <KeyboardAvoidingView
        style={styles.screen}
        behavior={Platform.OS === "ios" ? "padding" : undefined}
      >
        <View style={styles.header}>
          <View>
            <Text style={styles.eyebrow}>VitraMind AI</Text>
            <Text style={styles.heading}>Panel de trabajo</Text>
          </View>

          <Pressable
            style={({ pressed }) => [styles.cleanButton, pressed && styles.pressed]}
            onPress={clearChat}
          >
            <Text style={styles.cleanButtonText}>Limpiar</Text>
          </Pressable>
        </View>

        <View style={[styles.workspace, isWide && styles.workspaceWide]}>
          {isWide && (
            <InsightPanel
              count={userMessagesCount}
              selectedMode={selectedMode}
              onModeChange={setSelectedMode}
              onSuggestion={sendMessage}
            />
          )}

          <View style={styles.chatShell}>
            <View style={styles.projectStrip}>
              <View style={styles.projectInfo}>
                <Text style={styles.projectLabel}>Proyecto activo</Text>
                <Text style={styles.projectTitle}>
                  IA_Areli / Asistente personal
                </Text>
              </View>

              <View style={styles.projectBadge}>
                <Text style={styles.projectBadgeText}>Local</Text>
              </View>
            </View>

            <View style={styles.statusBand}>
              <View style={styles.statusItem}>
                <Text style={styles.statusLabel}>Modo</Text>
                <Text style={styles.statusValue}>Técnico</Text>
              </View>

              <View style={styles.statusDivider} />

              <View style={styles.statusItem}>
                <Text style={styles.statusLabel}>Contexto</Text>
                <Text style={styles.statusValue}>{userMessagesCount} mensajes</Text>
              </View>

              <View style={styles.statusDivider} />

              <View style={styles.statusItem}>
                <Text style={styles.statusLabel}>Tono</Text>
                <Text style={styles.statusValue}>{selectedModeLabel}</Text>
              </View>
            </View>

            {!isWide && (
              <ScrollView
                horizontal
                showsHorizontalScrollIndicator={false}
                style={styles.modeArea}
              >
                {USER_MODES.map((mode) => (
                  <ModeChip
                    key={mode.id}
                    mode={mode}
                    active={mode.id === selectedMode}
                    onPress={() => setSelectedMode(mode.id)}
                  />
                ))}
              </ScrollView>
            )}

            <ScrollView
              horizontal
              showsHorizontalScrollIndicator={false}
              style={styles.quickArea}
            >
              {QUICK_AREAS.map((area) => (
                <QuickChip
                  key={area}
                  label={area}
                  onPress={() => sendMessage(`Ayúdame con ${area}`)}
                />
              ))}
            </ScrollView>

            <ScrollView
              ref={scrollRef}
              style={styles.chat}
              contentContainerStyle={styles.chatContent}
              showsVerticalScrollIndicator={false}
            >
              {messages.map((message) => (
                <MessageBubble key={message.id} message={message} />
              ))}

              {messages.length === 1 && !isWide && (
                <View style={styles.suggestionPanel}>
                  <Text style={styles.suggestionTitle}>Ideas para empezar</Text>

                  {SUGGESTIONS.map((suggestion) => (
                    <Pressable
                      key={suggestion}
                      style={({ pressed }) => [
                        styles.suggestionButton,
                        pressed && styles.pressed,
                      ]}
                      onPress={() => sendMessage(suggestion)}
                    >
                      <Text style={styles.suggestionText}>{suggestion}</Text>
                    </Pressable>
                  ))}

                  <Text style={styles.suggestionTitleAlt}>
                    Qué podemos agregar
                  </Text>

                  {FEATURE_IDEAS.slice(0, 4).map((idea) => (
                    <View key={idea} style={styles.mobileIdeaItem}>
                      <Text style={styles.mobileIdeaText}>{idea}</Text>
                    </View>
                  ))}
                </View>
              )}
            </ScrollView>

            <View style={styles.composer}>
              <TextInput
                style={styles.input}
                value={input}
                onChangeText={setInput}
                placeholder="Escribe una duda, error, tarea o idea..."
                placeholderTextColor="#7C8798"
                multiline
              />

              <Pressable
                style={({ pressed }) => [
                  styles.sendButton,
                  !input.trim() && styles.sendButtonDisabled,
                  pressed && input.trim() && styles.pressed,
                ]}
                onPress={() => sendMessage()}
                disabled={!input.trim()}
              >
                <Text style={styles.sendButtonText}>Enviar</Text>
              </Pressable>
            </View>
          </View>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const SHADOW = {
  shadowColor: "#0F172A",
  shadowOffset: { width: 0, height: 8 },
  shadowOpacity: 0.08,
  shadowRadius: 18,
  elevation: 4,
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: COLORS.bg,
  },
  screen: {
    flex: 1,
    paddingHorizontal: 18,
    paddingTop: 14,
  },

  header: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between",
    paddingBottom: 16,
  },
  eyebrow: {
    color: COLORS.primary,
    fontSize: 12,
    fontWeight: "900",
    letterSpacing: 0.7,
    textTransform: "uppercase",
  },
  heading: {
    color: COLORS.text,
    fontSize: 27,
    fontWeight: "900",
    marginTop: 2,
  },
  cleanButton: {
    alignItems: "center",
    backgroundColor: COLORS.primary,
    borderRadius: 14,
    justifyContent: "center",
    paddingHorizontal: 16,
    paddingVertical: 11,
    ...SHADOW,
  },
  cleanButtonText: {
    color: "#FFFFFF",
    fontSize: 13,
    fontWeight: "900",
  },

  workspace: {
    flex: 1,
  },
  workspaceWide: {
    alignSelf: "center",
    flexDirection: "row",
    gap: 18,
    maxWidth: 1220,
    width: "100%",
  },

  chatShell: {
    flex: 1,
  },

  projectStrip: {
    alignItems: "center",
    backgroundColor: COLORS.card,
    borderColor: COLORS.border,
    borderRadius: 18,
    borderWidth: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 12,
    paddingHorizontal: 16,
    paddingVertical: 14,
    ...SHADOW,
  },
  projectInfo: {
    flex: 1,
    paddingRight: 12,
  },
  projectLabel: {
    color: COLORS.muted,
    fontSize: 11,
    fontWeight: "900",
    textTransform: "uppercase",
  },
  projectTitle: {
    color: COLORS.text,
    fontSize: 15,
    fontWeight: "900",
    marginTop: 3,
  },
  projectBadge: {
    backgroundColor: COLORS.successSoft,
    borderColor: "#B8E4D9",
    borderRadius: 999,
    borderWidth: 1,
    paddingHorizontal: 12,
    paddingVertical: 7,
  },
  projectBadgeText: {
    color: COLORS.success,
    fontSize: 12,
    fontWeight: "900",
  },

  statusBand: {
    alignItems: "center",
    backgroundColor: COLORS.card,
    borderColor: COLORS.border,
    borderRadius: 18,
    borderWidth: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    paddingHorizontal: 16,
    paddingVertical: 13,
    ...SHADOW,
  },
  statusItem: {
    flex: 1,
  },
  statusLabel: {
    color: COLORS.muted,
    fontSize: 12,
    fontWeight: "800",
  },
  statusValue: {
    color: COLORS.text,
    fontSize: 14,
    fontWeight: "900",
    marginTop: 2,
  },
  statusDivider: {
    backgroundColor: COLORS.border,
    height: 34,
    marginHorizontal: 10,
    width: 1,
  },

  quickArea: {
    flexGrow: 0,
    marginTop: 12,
    maxHeight: 42,
  },
  quickChip: {
    alignItems: "center",
    backgroundColor: COLORS.primarySoft,
    borderColor: "#C7DCF5",
    borderRadius: 999,
    borderWidth: 1,
    height: 38,
    justifyContent: "center",
    marginRight: 8,
    paddingHorizontal: 15,
  },
  quickChipText: {
    color: COLORS.primary,
    fontSize: 13,
    fontWeight: "900",
  },

  modeArea: {
    flexGrow: 0,
    marginTop: 10,
    maxHeight: 40,
  },
  modeWrap: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 8,
    marginTop: 10,
  },
  modeChip: {
    backgroundColor: "#F8FAFC",
    borderColor: COLORS.border,
    borderRadius: 999,
    borderWidth: 1,
    height: 34,
    justifyContent: "center",
    marginRight: 8,
    paddingHorizontal: 12,
  },
  modeChipActive: {
    backgroundColor: COLORS.primary,
    borderColor: COLORS.primary,
  },
  modeChipText: {
    color: COLORS.primary,
    fontSize: 12,
    fontWeight: "900",
  },
  modeChipTextActive: {
    color: "#FFFFFF",
  },
  modeDescription: {
    color: "#D7E4F5",
    fontSize: 12,
    fontWeight: "700",
    lineHeight: 18,
    marginTop: 9,
  },

  chat: {
    flex: 1,
    marginTop: 14,
  },
  chatContent: {
    paddingBottom: 18,
  },
  messageRow: {
    alignItems: "flex-start",
    marginBottom: 12,
  },
  messageRowUser: {
    alignItems: "flex-end",
  },
  bubble: {
    borderRadius: 18,
    maxWidth: "90%",
    paddingHorizontal: 15,
    paddingVertical: 13,
  },
  assistantBubble: {
    backgroundColor: COLORS.card,
    borderColor: COLORS.border,
    borderWidth: 1,
    ...SHADOW,
  },
  userBubble: {
    backgroundColor: COLORS.primary,
    ...SHADOW,
  },
  messageMeta: {
    borderBottomColor: "#E8EEF6",
    borderBottomWidth: 1,
    marginBottom: 8,
    paddingBottom: 7,
  },
  areaText: {
    color: COLORS.warning,
    fontSize: 11,
    fontWeight: "900",
    textTransform: "uppercase",
  },
  titleText: {
    color: COLORS.text,
    fontSize: 15,
    fontWeight: "900",
    marginTop: 2,
  },
  messageText: {
    color: "#243044",
    fontSize: 15,
    lineHeight: 22,
  },
  userMessageText: {
    color: "#FFFFFF",
    fontWeight: "700",
  },

  chipWrap: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 7,
    marginTop: 11,
  },
  insightChip: {
    backgroundColor: COLORS.successSoft,
    borderColor: "#B8E4D9",
    borderRadius: 999,
    borderWidth: 1,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  insightChipText: {
    color: COLORS.success,
    fontSize: 11,
    fontWeight: "900",
  },
  actionChip: {
    backgroundColor: COLORS.warningSoft,
    borderColor: "#FED7AA",
    borderRadius: 999,
    borderWidth: 1,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  actionChipText: {
    color: "#9A3412",
    fontSize: 12,
    fontWeight: "900",
  },

  composer: {
    alignItems: "flex-end",
    backgroundColor: COLORS.bg,
    borderTopColor: COLORS.border,
    borderTopWidth: 1,
    flexDirection: "row",
    gap: 10,
    paddingBottom: 12,
    paddingTop: 12,
  },
  input: {
    backgroundColor: "#FFFFFF",
    borderColor: "#C3CCD9",
    borderRadius: 18,
    borderWidth: 1,
    color: COLORS.text,
    flex: 1,
    fontSize: 15,
    maxHeight: 112,
    minHeight: 48,
    paddingHorizontal: 14,
    paddingVertical: 12,
  },
  sendButton: {
    alignItems: "center",
    backgroundColor: COLORS.primary,
    borderRadius: 16,
    height: 48,
    justifyContent: "center",
    paddingHorizontal: 18,
    ...SHADOW,
  },
  sendButtonDisabled: {
    backgroundColor: COLORS.disabled,
    shadowOpacity: 0,
    elevation: 0,
  },
  sendButtonText: {
    color: "#FFFFFF",
    fontSize: 14,
    fontWeight: "900",
  },

  suggestionPanel: {
    backgroundColor: COLORS.card,
    borderColor: COLORS.border,
    borderRadius: 18,
    borderWidth: 1,
    marginTop: 8,
    padding: 14,
    ...SHADOW,
  },
  suggestionTitle: {
    color: COLORS.text,
    fontSize: 14,
    fontWeight: "900",
    marginBottom: 8,
  },
  suggestionButton: {
    backgroundColor: "#F8FAFC",
    borderColor: COLORS.border,
    borderRadius: 14,
    borderWidth: 1,
    marginTop: 8,
    paddingHorizontal: 12,
    paddingVertical: 11,
  },
  suggestionText: {
    color: "#273142",
    fontSize: 14,
    fontWeight: "800",
  },
  suggestionTitleAlt: {
    color: COLORS.text,
    fontSize: 14,
    fontWeight: "900",
    marginBottom: 8,
    marginTop: 16,
  },
  mobileIdeaItem: {
    backgroundColor: "#F8FAFC",
    borderColor: COLORS.border,
    borderRadius: 14,
    borderWidth: 1,
    marginTop: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  mobileIdeaText: {
    color: "#273142",
    fontSize: 13,
    fontWeight: "700",
    lineHeight: 18,
  },

  insightPanel: {
    backgroundColor: COLORS.primaryDark,
    borderRadius: 22,
    padding: 18,
    width: 330,
    ...SHADOW,
  },
  panelEyebrow: {
    color: "#BFDBFE",
    fontSize: 12,
    fontWeight: "900",
    textTransform: "uppercase",
  },
  panelTitle: {
    color: "#FFFFFF",
    fontSize: 26,
    fontWeight: "900",
    lineHeight: 31,
    marginTop: 8,
  },
  panelCopy: {
    color: "#D7E4F5",
    fontSize: 14,
    lineHeight: 21,
    marginTop: 10,
  },
  metricRow: {
    flexDirection: "row",
    gap: 10,
    marginTop: 18,
  },
  metricBox: {
    backgroundColor: "#1F5F9F",
    borderRadius: 16,
    flex: 1,
    padding: 13,
  },
  metricBoxAlt: {
    backgroundColor: COLORS.success,
    borderRadius: 16,
    flex: 1,
    padding: 13,
  },
  metricValue: {
    color: "#FFFFFF",
    fontSize: 24,
    fontWeight: "900",
  },
  metricLabel: {
    color: "#EAF3FF",
    fontSize: 12,
    fontWeight: "800",
    marginTop: 2,
  },
  focusBox: {
    backgroundColor: "rgba(255,255,255,0.08)",
    borderColor: "rgba(255,255,255,0.13)",
    borderRadius: 16,
    borderWidth: 1,
    gap: 10,
    marginTop: 16,
    padding: 12,
  },
  infoLine: {
    alignItems: "flex-start",
    flexDirection: "row",
    gap: 9,
  },
  infoNumber: {
    color: "#BFDBFE",
    fontSize: 12,
    fontWeight: "900",
    width: 24,
  },
  infoText: {
    color: "#EAF3FF",
    flex: 1,
    fontSize: 12,
    fontWeight: "700",
    lineHeight: 17,
  },
  panelSection: {
    color: "#FFFFFF",
    fontSize: 14,
    fontWeight: "900",
    marginTop: 22,
  },
  sideSuggestion: {
    backgroundColor: "rgba(255,255,255,0.08)",
    borderColor: "rgba(255,255,255,0.13)",
    borderRadius: 15,
    borderWidth: 1,
    marginTop: 9,
    paddingHorizontal: 12,
    paddingVertical: 11,
  },
  sideSuggestionText: {
    color: "#F8FAFC",
    fontSize: 13,
    fontWeight: "800",
    lineHeight: 18,
  },
  ideaItem: {
    backgroundColor: "rgba(255,255,255,0.08)",
    borderLeftColor: "#F59E0B",
    borderLeftWidth: 3,
    borderRadius: 15,
    marginTop: 9,
    paddingHorizontal: 11,
    paddingVertical: 10,
  },
  ideaText: {
    color: "#EAF3FF",
    fontSize: 12,
    fontWeight: "700",
    lineHeight: 17,
  },

  pressed: {
    opacity: 0.72,
  },
});
