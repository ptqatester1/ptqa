##########################################################
##Author: AbbasH
#@summary: PDU Details
##########################################################

class PduConst:
    CLOSE_BUTTON = ':btn_close_HTML_Object'

    class ComplexPDU:
        SOURCE_DEVICE = ':sourceDevice_text_HTML_Object'
        AUTO_SELECT_PORT = ':autoSelectPort_checkbox_HTML_Object'
        OUTGOING_PORT = ':outgoingPort_select_HTML_Object'
        APPLICATION = ':application_select_HTML_Object'
        DESTINATION_IP = ':destinationIP_text_HTML_Object'
        SOURCE_IP = ':sourceIP_text_HTML_Object'
        TOS = ':tos_numField_HTML_Object'
        TTL = ':ttl_numField_HTML_Object'
        SEQ_NUM = ':sequence_numField_HTML_Object'
        SIZE = ':size_numField_HTML_Object'
        ONE_SHOT_RADIO = ':oneShot_radio_HTML_Object'
        ONE_SHOT_TIME = ':oneShot_textField_HTML_Object'
        PERIODIC_RADIO = ':periodic_radio_HTML_Object'
        PERIODIC_TIME = ':periodic_textField_HTML_Object'
        CREATE_PDU = ':send_button_HTML_Object'


    class PduTabs:
        OSI_LAYERS = ':piv_tab_bar_button_osi_HTML_Object'
        PDU_IN_DETAILS = ':piv_tab_bar_button_in_HTML_Object'
        PDU_OUT_DETAILS = ':piv_tab_bar_button_out_HTML_Object'
        EVENT_LIST = ':piv_tab_bar_button_event_list_HTML_Object'

    class OsiLayers:
        HEADER_INFO = ''
        EXPLANATION = ':items_HTML_Object'

        class InLayers:
            LAYER_1 = ':piv_tab_osi_ilayer_1_HTML_Object'
            LAYER_2 = ':piv_tab_osi_ilayer_2_HTML_Object'
            LAYER_3 = ':piv_tab_osi_ilayer_3_HTML_Object'
            LAYER_4 = ':piv_tab_osi_ilayer_4_HTML_Object'
            LAYER_5 = ':piv_tab_osi_ilayer_5_HTML_Object'
            LAYER_6 = ':piv_tab_osi_ilayer_6_HTML_Object'
            LAYER_7 = ':piv_tab_osi_ilayer_7_HTML_Object'

        class OutLayers:
            LAYER_1 = ':piv_tab_osi_olayer_1_HTML_Object'
            LAYER_2 = ':piv_tab_osi_olayer_2_HTML_Object'
            LAYER_3 = ':piv_tab_osi_olayer_3_HTML_Object'
            LAYER_4 = ':piv_tab_osi_olayer_4_HTML_Object'
            LAYER_5 = ':piv_tab_osi_olayer_5_HTML_Object'
            LAYER_6 = ':piv_tab_osi_olayer_6_HTML_Object'
            LAYER_7 = ':piv_tab_osi_olayer_7_HTML_Object'

    class Inbound:

        class FrameRelay:
            HEADER = ''
            FLG_START = ''
            ADDRESS = ''
            DATA = ''
            FCS = ''
            FLG_END = ''    
        
        class Arp:
            SOURCE_IP = ''    
            DESTINATION_IP = '' 

        class Http:
            DATA = ''           

        class Rstp:
            TYPE = ''
            HEADER = ''
        
        class Ethernet:    
            HEADER = ''
            PREAMBLE = ''
            DEST_MAC = ''
            SRC_MAC = ''
            TYPE = ''
            DATA = ''
            FCS = ''

        class Icmp:
            HEADER = ''
            TYPE = ''
            CODE = ''
            CHECKSUM = ''
            ID = ''
            SEQ_NUM = ''            

        class Icmpv6:    
            HEADER = ''
            TYPE = ''
            CODE = ''
            CHECKSUM = ''
            ID = ''
            SEQ_NUM = ''

            class Echo:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                ID = ''
                SEQ_NUM = ''
        
            class Neighbor:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                R = ''
                S = ''
                O = ''
                RESERVED = ''
                TARGET_ADDR = ''

            class PacketTooBig:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                MTU = ''                                

        class Rtp:
            RTP_HEADER = ''

        class Stp:          
            BPDU_PROTOCOL_ID = ''
            BPDU_VERSION = ''
            BPDU_BRIDGE_ID = ''         

        class Hdlc:
            HEADER = ''
            FLG_START = ''
            ADR = ''
            CONTROL = ''
            DATA = ''
            FCS = ''
            FLG_END = ''

        class LinkLayer:
            HEADER = ''
            TYPE = ''
            LENGTH = ''
            LINK_LAYER_ADDR = ''
            ADD = ''    

        class Ipv6:    
            HEADER = ''
            VER = ''
            TRFC = ''
            FLOW_LABEL = ''
            PL = ''
            NEXT = ''
            HOP_LIMIT = ''
            SRC_IP = ''
            DST_IP = ''
            DATA = ''

        class Ftp:
            HEADER = ''
            ARGUMENT = ''
            COMMAND = ''    

        class Tcp:    
            HEADER = ''
            SRC_PORT = ''
            DEST_PORT = ''
            SEQ_NUM = ''
            ACK_NUM = ''
            OFF = ''
            RES = ''
            SYN = ''
            WINDOW = ''
            CHECKSUM = ''
            URGENT_POINTER = ''
            OPTION = ''
            PADDING = ''
            DATE = ''                                       

        class Llc:    
            HEADER = ''
            DSAP = ''
            SSAP = ''
            CONTROL_BIT = ''    

        class Snap:    
            HEADER = ''
            OUI = ''
            PID = ''

        class Vtp:    
            HEADER = ""
            VERSION = ''
            CODE = ''
            FOLLOWERS = ''
            MGT_DOMAIN_LEN = ''
            MANAGEMENT_DOMAIN_NAME = ''
            CONFIGURATION_REVISION = ''
            UPDATER_ID = ''
            UPDATE_TIMESTAMP = ''
            MD5_DIGEST = '' 
        
        class Ppp:
            HEADER = ''
            FLG_START = ''
            ADR = ''
            CTR = ''
            PROTOCOL = ''
            LCP = ''
            FCS = ''
            FLG_END = ''

        class Ppoe:    
            HEADER = '' 

        class Dns:    
            HEADER_REGION = ''
            QUERY_REGION = ''

            class Option:
                HEADER = ''
                OPTION_DNS_SERVERS = ''
                LENGTH = ''
                DNS_SERVER = ''

            class ANSWER2:
                HEADER = ''
                NAME = ''
                TYPE = ''
                CLASS = ''
                TTL = ''
                LENGTH = ''
                ADDRESS = ''
                
            class ANSWER3:
                HEADER = ''
                NAME = ''
                TYPE = ''
                CLASS = ''
                TTL = ''
                LENGTH = ''
                ADDRESS = ''

        class Tcp:
            HEADER = ''
            SRC_PORT = ''
            DEST_PORT = ''
            SRC_IP = ''
            DST_IP = ''
            GRE_SRC_IP = ''
            GRE_DST_IP = ''         
            SEQ_NUM = ''
            ACK_NUM = ''
            OFF = ''
            RES = ''
            SYN = ''
            WINDOW = ''
            CHECKSUM = ''
            URGENT_POINTER = ''
            OPTION = ''
            PADDING = ''
            DATE = ''                                                                                       

        class Wireless_802_11:
            HEADER = ''
            FRAME_CONTROL = ''
            DURATION_ID = ''
            ADDRESS_1 = ''
            ADDRESS_2 = ''
            ADDRESS_3 = ''
            ADDRESS_4 = ''
            SEQUENCE_CONTROL = ''
            DATA = ''
            FCS = ''

        class Isakmp:   
            HEADER = ''
            INITIATOR_COOKIE = ''
            RESPONDER_COOKIE = ''
            NEXT_PAYLOAD = ''
            VERSION = ''
            EXCHANGE_TYPE = ''
            FLAG = ''
            MESSAGE_ID = ''
            LENGTH = ''

            SECURITY_ASSOCIATION_HEADER = ''
            SECURITY_ASSOCIATION_NEXT_PAYLOAD = ''
            SECURITY_ASSOCIATION_RESERVED = ''
            SECURITY_ASSOCIATION_PAYLOAD_LENGTH = ''
            SECURITY_ASSOCIATION_DOMAIN = ''
            SECURITY_ASSOCIATION_SITUATION = ''
        
            PROPOSAL_PAYLOAD_1_HEADER = ''
            PROPOSAL_PAYLOAD_1_NEXT_PAYLOAD = ''
            PROPOSAL_PAYLOAD_1_RESERVED = ''
            PROPOSAL_PAYLOAD_1_PAYLOAD_LENGTH = ''
            PROPOSAL_PAYLOAD_1_PROPOSAL = ''
            PROPOSAL_PAYLOAD_1_PROTOCOL_ID = ''
            PROPOSAL_PAYLOAD_1_SPI_SIZE = ''
            PROPOSAL_PAYLOAD_1_NUM_TRANSFORM = ''
            PROPOSAL_PAYLOAD_1_SPI = ''
        
            TRANSFORM_PAYLOAD_1_HEADER = ''
            TRANSFORM_PAYLOAD_1_NEXT_PAYLOAD = ''
            TRANSFORM_PAYLOAD_1_PAYLOAD_LENGTH = ''
            TRANSFORM_PAYLOAD_1_TRANSFORM_NUM = ''
            TRANSFORM_PAYLOAD_1_TRANSFORM_ID = ''
            TRANSFORM_PAYLOAD_1_ENCRYPTION_ALGORITHM = ''
            TRANSFORM_PAYLOAD_1_KEYLENGTH = ''
            TRANSFORM_PAYLOAD_1_HASH_ALGORITHM = ''
            TRANSFORM_PAYLOAD_1_GROUP_DESCRIPTION = ''
            TRANSFORM_PAYLOAD_1_AUTHENTICATION_METHOD =  ''
            TRANSFORM_PAYLOAD_1_LIFE_TYPE = ''
            TRANSFORM_PAYLOAD_1_LIFE_DURATION = ''
            
            VENDOR_ID_PAYLOAD_HEADER = ''
            VENDOR_ID_PAYLOAD_NEXT_PAYLOAD = ''
            VENDOR_ID_PAYLOAD_RESERVED = ''
            VENDOR_ID_PAYLOAD_LENGTH = ''
            VENDOR_ID_PAYLOAD_VENDOR_ID = ''
            
            KEY_EXCHANGE_PAYLOAD_HEADER = ''
            KEY_EXCHANGE_PAYLOAD_NEXT_PAYLOAD = ''
            KEY_EXCHANGE_PAYLOAD_RESERVED = ''
            KEY_EXCHANGE_PAYLOAD_LENGTH = ''
            KEY_EXCHANGE_PAYLOAD = ''
            
            NONCE_PAYLOAD_HEADER = ''
            NONCE_PAYLOAD_NEXT_PAYLOAD = ''
            NONCE_PAYLOAD_RESERVED = ''
            NONCE_PAYLOAD_LENGTH = ''
            NONCE_PAYLOAD = ''
            
            ENCRYPTED_PAYLOAD_HEADER = ''
            ENCRYPTED_PAYLOAD = ''

        class EthernetII:                               
            HEADER = ''
            PREAMBLE = ''
            DEST_MAC = ''
            SRC_MAC = ''
            TYPE = ''
            DATA = ''
            FCS = ''
            
            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_4 = ''
            BITS_LABEL_5 = ''
            BITS_LABEL_6 = ''
            BITS_UNITS_LABEL = ''

        class Ip:
            HEADER = ''
            VER = ''
            IHL = ''
            DSCP = ''
            TL = ''
            ID = ''
            FLAG = ''
            FRAG_OFFSET = ''
            TTL = ''
            PRO = ''
            CHKSUM = ''
            SRC_IP = ''
            DST_IP = ''
            OPT = ''
            PADDING = ''
            DATA = ''

            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_2_2 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_3_2 = ''
            BITS_LABEL_4 = ''
            BITS_UNITS_LABEL = ''   

        class Udp:
            HEADER = ''
            SRC_PORT = ''
            DST_PORT = ''
            LENGTH = ''
            CHECKSUM = ''
            DATA = ''           
            DNS_HEADER = ''                                 

            BITS_LABEL_1 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_3_2_2 = ''
            BITS_UNITS_LABEL = ''

        class Dhcp:
            HEADER = '' 
            OP = ''
            HW_TYPE = ''
            HW_LEN = ''
            TXT_HOPS = '' 
            TRANSACTION_ID = ''
            SECS = ''
            FLAG = ''
            CLIENT_ADDRESS = ''
            YOUR_CLIENT_ADDRESS = ''
            SERVER_ADDRESS = ''
            RELAY_AGENT_ADDRESS = ''
            CLIENT_HARDWARE_ADDRESS = ''
            SERVER_HOSTNAME = ''
            FILE = ''
            OPTIONS = ''
            
            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_4 = ''
            BITS_UNITS_LABEL = ''   

        class Eigrp:
            HEADER = ''
            VER = ''
            OPC = ''
            CHECKSUM = ''
            FLAG = ''
            SEQ_NUM = ''
            ACKNUM = ''
            AUTONOMOUS_SN = ''
            TYPE = ''
            LENGTH = ''
            K1 = ''
            K2 = ''
            K3 = ''
            K4 = ''
            K5 = ''
            RES = ''
            HOLD_TIME = ''
            SOFT_TYPE = ''
            SOFT_LENGTH = ''
            IOS_VER = ''
            VER = ''        
        
        class Template: 
            FLOWSET = ''
            FLOWHEADER = '' 
            FLOWTEMPLATE = ''
        
        class Data: 
            FLOWSET = ''
            LENGTH = ''
            FLOWSET_ID = '' 
            INTERFACE_INPUT = ''
            TRNS_SOURCE_PORT = ''
            TRNS_DESTINATION_PORT = ''
            TOS = ''
            PROTOCOL = ''
            FLOW_SAMPLER_ID = ''
            IPV4_SOURCE_MASK = ''
            IPV4_DESTINATION_MASK = ''
            COUNTER_BYTES = ''
            IPV4_NEXT_HOP_ADDRESS = ''
            FLAGS = ''
            INTERFACE_OUTPUT = ''
            COUNTER_PACKETS = ''
            SOURCE_AS = ''
            DESTINATION_AS = ''             

        class NetFlow:
            class NetFlowVersion9Header:
                HEADER = ''
                VERSION = ''
                COUNT = ''
                SYS_UP_TIME = ''
                CURRENT_SECS = ''
                FLOW_SEQUENCE = ''
                SOURCE_ID = ''
                
            class TemplateFlowSet:
                HEADER = ''
                ID = ''
                ID_LENGTH = ''
                TEMPLATE_ID = ''
                TEMPLATE_ID_COUNT = ''

                MATCH_SOURCE_IP = ''
                MATCH_SOURCE_IP_LENGTH = ''
                MATCH_SOURCE_IP_LENGTH_4 = ''
                MATCH_DEST_IP = ''
                MATCH_DEST_IP_LENGTH = ''
                MATCH_DEST_IP_LENGTH_4 = ''
                MATCH_INT_INPUT = ''
                MATCH_INT_INPUT_LENGTH = ''
                MATCH_TRANSPORT_SOURCE = ''
                MATCH_TRANSPORT_SOURCE_LENGTH = ''
                MATCH_TRANSPORT_DEST = ''
                MATCH_TRANSPORT_DEST_LENGTH = ''
                MATCH_IP_TOS = ''
                MATCH_IP_TOS_LENGTH = ''
                MATCH_IP_PRO = ''
                MATCH_IP_PRO_LENGTH = ''
                MATCH_FLOW_SAMPLER = ''
                MATCH_FLOW_SAMPLER_LENGTH = ''
                MATCH_FLOW_DIRECTION = ""
                MATCH_FLOW_DIRECTION_LENGTH = ""
                COLLECT_IP_SOURCE_MASK = ''
                COLLECT_IP_SOURCE_MASK_LENGTH = ''
                COLLECT_IP_DEST_MASK = ''
                COLLECT_IP_DEST_MASK_LENGTH = ''
                COLLECT_COUNTER_BYTES = ''
                COLLECT_COUNTER_BYTES_LENGTH = ''
                COLLECT_NEXT_HOP = ''
                COLLECT_NEXT_HOP_LENGTH = ''
                COLLECT_TRANSPORT_TCP = ''
                COLLECT_TRANSPORT_TCP_LENGTH = ''
                COLLECT_INT_OUTPUT = ''
                COLLECT_INT_OUTPUT_LENGTH = ''
                COLLECT_COUNTER_PACKETS = ''
                COLLECT_COUNTER_PACKETS_LENGTH = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_FIRST = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_FIRST_LENGTH = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_LAST = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_LAST_LENGTH = ''
                COLLECT_ROUTING_SOURCE = ''
                COLLECT_ROUTING_SOURCE_LENGTH = ''
                COLLECT_ROUTING_DEST = ''
                COLLECT_ROUTING_DEST_LENGTH = ''
                
                ##IPv6 constants
                MATCH_IPV6_DEST = ''
                MATCH_IPV6_DEST_LENGTH = ''
                MATCH_IPV6_SOURCE = ''
                MATCH_IPV6_SOURCE_LENGTH = ''
                MATCH_IPV6_PRO = ''
                MATCH_IPV6_PRO_LENGTH = ''
                COLLECT_IPV6_DEST_MASK = ''
                COLLECT_IPV6_DEST_MASK_LENGTH = ''
                COLLECT_IPV6_SOURCE_MASK = ''
                COLLECT_IPV6_SOURCE_MASK_LENGTH = ''
                
            class DataFlowSet:
                HEADER = ''
                ID = ''
                LENGTH = ''

                IPV4_SOURCE_ADD = ''
                IPV4_DEST_ADD = ''
                INT_INPUT = ''
                TRNS_SOURCE_PORT = ''
                TRNS_DEST_PORT = ''
                IP_TOS = ''
                IP_PROTOCOL = ''
                FLOW_SAMPLER_ID = ''
                FLOW_DIRECTION = ''
                IP_SOURCE_MASK = ''
                IP_DEST_MASK = ''
                COUNTER_BYTES = ''
                IP_NEXT_HOP = ''
                TCP_FLAGS = ''
                INT_OUTPUT = ''
                COUNTER_PACKETS = ''
                TIMESTAMP_FIRST = ''
                TIMESTAMP_LAST = ''
                IP_SOURCE_AS = ''
                IP_DEST_AS = ''
                PADDING = ''
    
                ##IPv6 constants
                IPV6_DEST = ''
                IPV6_SOURCE = ''
                IPV6_DEST_MASK = ''
                IPV6_SOURCE_MASK = ''                               

        class Dhcpv6:

            class SolicitMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ElapsedTimeOption:
                HEADER = ''
                OPTION_ELAPSED_TIME = ''
                LENGTH = ''
                ELAPSED_TIME = ''

            class ClientIDOption:
                HEADER = ''
                OPTION_CLIENT_ID = ''
                LENGTH = ''
                DUID = ''

            class RequestOption:
                HEADER = ''
                OPTION_ORO = ''
                LENGTH = ''
                REQUEST_OPTION_CODE1 = ''
                REQUEST_OPTION_CODE2 = ''
                REQUEST_OPTION_CODE3 = ''
            
            class IAPdOption:
                HEADER = ''
                OPTION_IA_PD = ''
                LENGTH = ''
                IAID = ''
                T1 = ''
                T2 = ''

            class IAPrefixOption:
                HEADER = ''
                OPTION_IAPREFIX = ''
                LENGTH = ''
                PREFERRED_LIFETIME = ''
                VALID_LIFETIME = ''
                PREFIX_LENGTH = ''
                IPV6_PREFIX = ''

            class RequestMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ServerIdOption:
                HEADER = ''
                OPTION_SERVER_ID = ''
                LENGTH = ''
                DUID = ''

            class DomainSearchOption:
                HEADER = ''
                FIELD1 = ''
                LEN = ''
                SEARCH_STRING = ''

            class AdvertiseMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ReplyMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class DNSOption:
                HEADER = ''
                OPTION_DNS_SERVERS = ''
                LENGTH = ''
                DNS_SERVER = ''


    class Outbound:

        class FrameRelay:
            HEADER = ''
            FLG_START = ''
            ADDRESS = ''
            DATA = ''
            FCS = ''
            FLG_END = ''
        
        class Arp:    
            DESTINATION_IP = ''
        
        class Http:    
            DATA = ''
        
        class Rstp: 
            TYPE = ''          
            HEADER = ''
        
        class Ethernet:    
            HEADER = ''
            PREAMBLE = ''
            DEST_MAC = ''
            SRC_MAC = ''
            TYPE = ''
            DATA = ''
            FCS = ''
        
        class Icmp:    
            HEADER = ''
            TYPE = ''
            CODE = ''
            CHECKSUM = ''
            ID = ''
            SEQ_NUM = ''
        
        class Icmpv6:    
            HEADER = ''
            TYPE = ''
            CODE = ''
            CHECKSUM = ''
            ID = ''
            SEQ_NUM = ''

            class Echo:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                ID = ''
                SEQ_NUM = ''
        
            class Neighbor:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                R = ''
                S = ''
                O = ''
                RESERVED = ''
                TARGET_ADDR = ''

            class PacketTooBig:
                HEADER = ''
                TYPE = ''
                CODE = ''
                CHECKSUM = ''
                MTU = ''
                    
        class Rtp:
            RTP_HEADER = ''
        
        class Stp:          
            BPDU_PROTOCOL_ID = ''
            BPDU_VERSION = ''
            BPDU_BRIDGE_ID = ''
        
        class Hdlc:
            HEADER = ''
            FLG_START = ''
            ADR = ''
            CONTROL = ''
            DATA = ''
            FCS = ''
            FLG_END = ''
        
        class LinkLayer:    
            HEADER = ''
            TYPE = ''
            LENGTH = ''
            LINK_LAYER_ADDR = ''
            ADD = ''
        
        class Ipv6:    
            HEADER = ''
            VER = ''
            TRFC = ''
            FLOW_LABEL = ''
            PL = ''
            NEXT = ''
            HOP_LIMIT = ''
            SRC_IP = ''
            DST_IP = ''
            DATA = ''

        class Ftp:
            HEADER = ''
            ARGUMENT = ''
            COMMAND = ''
        
        class Tcp:    
            HEADER = ''
            SRC_PORT = ''
            DEST_PORT = ''
            SEQ_NUM = ''
            ACK_NUM = ''
            OFF = ''
            RES = ''
            SYN = ''
            WINDOW = ''
            CHECKSUM = ''
            URGENT_POINTER = ''
            OPTION = ''
            PADDING = ''
            DATE = ''
        
        class Llc:    
            HEADER = ''
            DSAP = ''
            SSAP = ''
            CONTROL_BIT = ''
        
        class Snap:    
            HEADER = ''
            OUI = ''
            PID = ''
        
        class Vtp:    
            HEADER = ""
            VERSION = ''
            CODE = ''
            FOLLOWERS = ''
            MGT_DOMAIN_LEN = ''
            MANAGEMENT_DOMAIN_NAME = ''
            CONFIGURATION_REVISION = ''
            UPDATER_ID = ''
            UPDATE_TIMESTAMP = ''
            MD5_DIGEST = ''
        
        class Ppp:    
            HEADER = ''
            FLG_START = ''
            ADR = ''
            CTR = ''
            PROTOCOL = ''
            LCP = ''
            FCS = ''
            FLG_END = ''
        
        class Ppoe:    
            HEADER = ''
        
        class Dns:    
            HEADER_REGION = ''
            QUERY_REGION = ''

            class Option:
                HEADER = ''
                OPTION_DNS_SERVERS = ''
                LENGTH = ''
                DNS_SERVER = ''

            class ANSWER2:
                HEADER = ''
                NAME = ''
                TYPE = ''
                CLASS = ''
                TTL = ''
                LENGTH = ''
                ADDRESS = ''
        
        class TCP:
            HEADER = ''
            SRC_PORT = ''
            DEST_PORT = ''
            SRC_IP = ''
            DST_IP = ''
            GRE_SRC_IP = ''
            GRE_DST_IP = ''         
            SEQ_NUM = ''
            ACK_NUM = ''
            OFF = ''
            RES = ''
            SYN = ''
            WINDOW = ''
            CHECKSUM = ''
            URGENT_POINTER = ''
            OPTION = ''
            PADDING = ''
            DATE = ''

        class Wireless_802_11:
            HEADER = ''
            FRAME_CONTROL = ''
            DURATION_ID = ''
            ADDRESS_1 = ''
            ADDRESS_2 = ''
            ADDRESS_3 = ''
            ADDRESS_4 = ''
            SEQUENCE_CONTROL = ''
            DATA = ''
            FCS = ''

        class Isakmp:
            HEADER = ''
            INITIATOR_COOKIE = ''
            RESPONDER_COOKIE = ''
            NEXT_PAYLOAD = ''
            VERSION = ''
            EXCHANGE_TYPE = ''
            FLAG = ''
            MESSAGE_ID = ''
            LENGTH = ''
            
            SECURITY_ASSOCIATION_HEADER = ''
            SECURITY_ASSOCIATION_NEXT_PAYLOAD = ''
            SECURITY_ASSOCIATION_RESERVED = ''
            SECURITY_ASSOCIATION_PAYLOAD_LENGTH = ''
            SECURITY_ASSOCIATION_DOMAIN = ''
            SECURITY_ASSOCIATION_SITUATION = ''
        
            PROPOSAL_PAYLOAD_1_HEADER = ''
            PROPOSAL_PAYLOAD_1_NEXT_PAYLOAD = ''
            PROPOSAL_PAYLOAD_1_RESERVED = ''
            PROPOSAL_PAYLOAD_1_PAYLOAD_LENGTH = ''
            PROPOSAL_PAYLOAD_1_PROPOSAL = ''
            PROPOSAL_PAYLOAD_1_PROTOCOL_ID = ''
            PROPOSAL_PAYLOAD_1_SPI_SIZE = ''
            PROPOSAL_PAYLOAD_1_NUM_TRANSFORM = ''
            PROPOSAL_PAYLOAD_1_SPI = ''
        
            TRANSFORM_PAYLOAD_1_HEADER = ''
            TRANSFORM_PAYLOAD_1_NEXT_PAYLOAD = ''
            TRANSFORM_PAYLOAD_1_PAYLOAD_LENGTH = ''
            TRANSFORM_PAYLOAD_1_TRANSFORM_NUM = ''
            TRANSFORM_PAYLOAD_1_TRANSFORM_ID = ''
            TRANSFORM_PAYLOAD_1_ENCRYPTION_ALGORITHM = ''
            TRANSFORM_PAYLOAD_1_KEYLENGTH = ''
            TRANSFORM_PAYLOAD_1_HASH_ALGORITHM = ''
            TRANSFORM_PAYLOAD_1_GROUP_DESCRIPTION = ''
            TRANSFORM_PAYLOAD_1_AUTHENTICATION_METHOD =  ''
            TRANSFORM_PAYLOAD_1_LIFE_TYPE = ''
            TRANSFORM_PAYLOAD_1_LIFE_DURATION = ''
            
            VENDOR_ID_PAYLOAD_HEADER = ''
            VENDOR_ID_PAYLOAD_NEXT_PAYLOAD = ''
            VENDOR_ID_PAYLOAD_RESERVED = ''
            VENDOR_ID_PAYLOAD_LENGTH = ''
            VENDOR_ID_PAYLOAD_VENDOR_ID = ''
            
            KEY_EXCHANGE_PAYLOAD_HEADER = ''
            KEY_EXCHANGE_PAYLOAD_NEXT_PAYLOAD = ''
            KEY_EXCHANGE_PAYLOAD_RESERVED = ''
            KEY_EXCHANGE_PAYLOAD_LENGTH = ''
            KEY_EXCHANGE_PAYLOAD = ''
            
            NONCE_PAYLOAD_HEADER = ''
            NONCE_PAYLOAD_NEXT_PAYLOAD = ''
            NONCE_PAYLOAD_RESERVED = ''
            NONCE_PAYLOAD_LENGTH = ''
            NONCE_PAYLOAD = ''
            
            ENCRYPTED_PAYLOAD_HEADER = ''
            ENCRYPTED_PAYLOAD = ''
        
        class EthernetII:
            HEADER = ''
            PREAMBLE = ''
            DEST_MAC = ''
            SRC_MAC = ''
            TYPE = ''
            DATA = ''
            FCS = ''
            
            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_4 = ''
            BITS_LABEL_5 = ''
            BITS_LABEL_6 = ''
            BITS_UNITS_LABEL = ''

        class Ip:
            HEADER = ''
            VER = ''
            IHL = ''
            DSCP = ''
            TL = ''
            ID = ''
            FLAG = ''
            FRAG_OFFSET = ''
            TTL = ''
            PRO = ''
            CHKSUM = ''
            SRC_IP = ''
            DST_IP = ''
            OPT = ''
            PADDING = ''
            DATA = ''

            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_2_2 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_3_2 = ''
            BITS_LABEL_4 = ''
            BITS_UNITS_LABEL = ''

        class Udp:
            HEADER = ''
            SRC_PORT = ''
            DEST_PORT = ''
            LENGTH = ''
            CHECKSUM = ''
            DATA = ''
            DNS_HEADER = ''
            
            BITS_LABEL_1 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_3_2_2 = ''
            BITS_UNITS_LABEL = ''

        class Dhcp:
            HEADER = '' 
            OP = ''
            HW_TYPE = ''
            HW_LEN = ''
            TXT_HOPS = '' 
            TRANSACTION_ID = ''
            SECS = ''
            FLAG = ''
            CLIENT_ADDRESS = ''
            YOUR_CLIENT_ADDRESS = ''
            SERVER_ADDRESS = ''
            RELAY_AGENT_ADDRESS = ''
            CLIENT_HARDWARE_ADDRESS = ''
            SERVER_HOSTNAME = ''
            FILE = ''
            OPTIONS = ''
            
            BITS_LABEL_1 = ''
            BITS_LABEL_2 = ''
            BITS_LABEL_3 = ''
            BITS_LABEL_4 = ''
            BITS_UNITS_LABEL = ''

        class Eigrp:
            HEADER = ''
            VER = ''
            OPC = ''
            CHECKSUM = ''
            FLAG = ''
            SEQ_NUM = ''
            ACKNUM = ''
            AUTONOMOUS_SN = ''
            TYPE = ''
            LENGTH = ''
            K1 = ''
            K2 = ''
            K3 = ''
            K4 = ''
            K5 = ''
            RES = ''
            HOLD_TIME = ''
            SOFT_TYPE = ''
            SOFT_LENGTH = ''
            IOS_VER = ''
            VER = ''        
        
        class Template: 
            FLOWSET = ''
            FLOWHEADER = '' 
            FLOWTEMPLATE = ''
        
        class Data: 
            FLOWSET = ''
            LENGTH = ''
            FLOWSET_ID = '' 
            INTERFACE_INPUT = ''
            TRNS_SOURCE_PORT = ''
            TRNS_DESTINATION_PORT = ''
            TOS = ''
            PROTOCOL = ''
            FLOW_SAMPLER_ID = ''
            IPV4_SOURCE_MASK = ''
            IPV4_DESTINATION_MASK = ''
            COUNTER_BYTES = ''
            IPV4_NEXT_HOP_ADDRESS = ''
            FLAGS = ''
            INTERFACE_OUTPUT = ''
            COUNTER_PACKETS = ''
            SOURCE_AS = ''
            DESTINATION_AS = ''         

        class NetFlow:
            class NetFlowVersion9Header:
                HEADER = ''
                VERSION = ''
                COUNT = ''
                SYS_UP_TIME = ''
                CURRENT_SECS = ''
                FLOW_SEQUENCE = ''
                SOURCE_ID = ''
                
            class TemplateFlowSet:
                HEADER = ''
                ID = ''
                ID_LENGTH = ''
                TEMPLATE_ID = ''
                TEMPLATE_ID_COUNT = ''

                MATCH_SOURCE_IP = ''
                MATCH_SOURCE_IP_LENGTH = ''
                MATCH_SOURCE_IP_LENGTH_4 = ''
                MATCH_DEST_IP = ''
                MATCH_DEST_IP_LENGTH = ''
                MATCH_DEST_IP_LENGTH_4 = ''
                MATCH_INT_INPUT = ''
                MATCH_INT_INPUT_LENGTH = ''
                MATCH_TRANSPORT_SOURCE = ''
                MATCH_TRANSPORT_SOURCE_LENGTH = ''
                MATCH_TRANSPORT_DEST = ''
                MATCH_TRANSPORT_DEST_LENGTH = ''
                MATCH_IP_TOS = ''
                MATCH_IP_TOS_LENGTH = ''
                MATCH_IP_PRO = ''
                MATCH_IP_PRO_LENGTH = ''
                MATCH_FLOW_SAMPLER = ''
                MATCH_FLOW_SAMPLER_LENGTH = ''
                MATCH_FLOW_DIRECTION = ""
                MATCH_FLOW_DIRECTION_LENGTH = ""
                COLLECT_IP_SOURCE_MASK = ''
                COLLECT_IP_SOURCE_MASK_LENGTH = ''
                COLLECT_IP_DEST_MASK = ''
                COLLECT_IP_DEST_MASK_LENGTH = ''
                COLLECT_COUNTER_BYTES = ''
                COLLECT_COUNTER_BYTES_LENGTH = ''
                COLLECT_NEXT_HOP = ''
                COLLECT_NEXT_HOP_LENGTH = ''
                COLLECT_TRANSPORT_TCP = ''
                COLLECT_TRANSPORT_TCP_LENGTH = ''
                COLLECT_INT_OUTPUT = ''
                COLLECT_INT_OUTPUT_LENGTH = ''
                COLLECT_COUNTER_PACKETS = ''
                COLLECT_COUNTER_PACKETS_LENGTH = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_FIRST = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_FIRST_LENGTH = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_LAST = ''
                COLLECT_TIMESTAMP_SYS_UPTIME_LAST_LENGTH = ''
                COLLECT_ROUTING_SOURCE = ''
                COLLECT_ROUTING_SOURCE_LENGTH = ''
                COLLECT_ROUTING_DEST = ''
                COLLECT_ROUTING_DEST_LENGTH = ''
                
                ##IPv6 constants
                MATCH_IPV6_DEST = ''
                MATCH_IPV6_DEST_LENGTH = ''
                MATCH_IPV6_SOURCE = ''
                MATCH_IPV6_SOURCE_LENGTH = ''
                MATCH_IPV6_PRO = ''
                MATCH_IPV6_PRO_LENGTH = ''
                COLLECT_IPV6_DEST_MASK = ''
                COLLECT_IPV6_DEST_MASK_LENGTH = ''
                COLLECT_IPV6_SOURCE_MASK = ''
                COLLECT_IPV6_SOURCE_MASK_LENGTH = ''
                
            class DataFlowSet:
                HEADER = ''
                ID = ''
                LENGTH = ''

                IPV4_SOURCE_ADD = ''
                IPV4_DEST_ADD = ''
                INT_INPUT = ''
                TRNS_SOURCE_PORT = ''
                TRNS_DEST_PORT = ''
                IP_TOS = ''
                IP_PROTOCOL = ''
                FLOW_SAMPLER_ID = ''
                FLOW_DIRECTION = ''
                IP_SOURCE_MASK = ''
                IP_DEST_MASK = ''
                COUNTER_BYTES = ''
                IP_NEXT_HOP = ''
                TCP_FLAGS = ''
                INT_OUTPUT = ''
                COUNTER_PACKETS = ''
                TIMESTAMP_FIRST = ''
                TIMESTAMP_LAST = ''
                IP_SOURCE_AS = ''
                IP_DEST_AS = ''
                PADDING = ''
    
                ##IPv6 constants
                IPV6_DEST = ''
                IPV6_SOURCE = ''
                IPV6_DEST_MASK = ''
                IPV6_SOURCE_MASK = ''

        class Dhcpv6:

            class SolicitMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ElapsedTimeOption:
                HEADER = ''
                OPTION_ELAPSED_TIME = ''
                LENGTH = ''
                ELAPSED_TIME = ''

            class ClientIDOption:
                HEADER = ''
                OPTION_CLIENT_ID = ''
                LENGTH = ''
                DUID = ''

            class RequestOption:
                HEADER = ''
                OPTION_ORO = ''
                LENGTH = ''
                REQUEST_OPTION_CODE1 = ''
                REQUEST_OPTION_CODE2 = ''
                REQUEST_OPTION_CODE3 = ''
            
            class IAPdOption:
                HEADER = ''
                OPTION_IA_PD = ''
                LENGTH = ''
                IAID = ''
                T1 = ''
                T2 = ''

            class IAPrefixOption:
                HEADER = ''
                OPTION_IAPREFIX = ''
                LENGTH = ''
                PREFERRED_LIFETIME = ''
                VALID_LIFETIME = ''
                PREFIX_LENGTH = ''
                IPV6_PREFIX = ''

            class RequestMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ServerIdOption:
                HEADER = ''
                OPTION_SERVER_ID = ''
                LENGTH = ''
                DUID = ''

            class DomainSearchOption:
                HEADER = ''
                FIELD1 = ''
                LEN = ''
                SEARCH_STRING = ''

            class AdvertiseMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class ReplyMessage:
                HEADER = ''
                TYPE = ''
                TRANSACTION_ID = ''
                OPTIONS = ''

            class DNSOption:
                HEADER = ''
                OPTION_DNS_SERVERS = ''
                LENGTH = ''
                DNS_SERVER = ''                
    
